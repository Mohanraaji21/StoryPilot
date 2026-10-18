import React, { useEffect, useState, useCallback } from "react";
const api = async (p, o) => { const r = await fetch("/api" + p, o); if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText); return r.json(); };
const post = (p, b) => api(p, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(b || {}) });
const Chip = ({ v }) => <span className={`chip ${v}`}>{String(v).replaceAll("_", " ")}</span>;
const Ev = ({ list, docs }) => list.map((e, i) => <blockquote key={i}><b>{e.source_id}</b> {docs?.[e.source_id] && `(${docs[e.source_id].name}, ${docs[e.source_id].version}, ${docs[e.source_id].date}, ${docs[e.source_id].origin})`}<br />“{e.excerpt}”</blockquote>);
export default function App() {
  const [tab, setTab] = useState("stories"), [sid, setSid] = useState(null), [err, setErr] = useState(""), [mode, setMode] = useState({});
  useEffect(() => { api("/mode").then(setMode).catch(e => setErr(e.message)); }, []);
  const open = id => { setSid(id); setTab("story"); };
  return <>
    <header><h1>StoryPilot</h1>
      <nav>{[["stories", "Today"], ["story", "Story"], ["queue", "Approval queue"], ["eval", "Evaluation"]].map(([k, l]) =>
        <button key={k} aria-current={tab === k} onClick={() => setTab(k)}>{l}</button>)}</nav>
      <span className="mode">AI: {mode.ai} ({mode.model}) · Store: {mode.store} · Data: {mode.source}</span></header>
    <main>{err && <div className="err" role="alert">{err}</div>}
      {tab === "stories" && <Stories open={open} setErr={setErr} mode={mode} />}
      {tab === "story" && (sid ? <Story sid={sid} setErr={setErr} /> : <p className="panel">Pick a story from Today to start.</p>)}
      {tab === "queue" && <Queue setErr={setErr} open={open} />}
      {tab === "eval" && <Eval setErr={setErr} />}</main></>;
}
function Stories({ open, setErr, mode }) {
  const [s, setS] = useState([]), [key, setKey] = useState(""), [busy, setBusy] = useState(false);
  const load = () => api("/stories").then(setS).catch(e => setErr(e.message)); useEffect(() => { load(); }, []);
  const imp = async () => { if (!key.trim()) return setErr("Enter a Jira issue key, for example PAY-123."); setBusy(true); setErr("");
    try { const r = await post("/import/jira", { key: key.trim() }); setKey(""); await load(); open(r.story_id); } catch (e) { setErr(e.message); } setBusy(false); };
  return <><div className="panel"><h2>Import from Jira and Confluence</h2>
    {mode.jira ? <><input aria-label="Jira issue key" placeholder="Jira issue key, e.g. PAY-123" value={key} onChange={e => setKey(e.target.value)} />
      <button className="act" disabled={busy} onClick={imp}>{busy ? "Importing…" : "Import story and related pages"}</button>
      <p className="note">Read-only. Related Confluence pages are found by keyword search and shown with their source, version and date.</p></>
      : <p className="note">Not configured. Set ATLASSIAN_BASE_URL, ATLASSIAN_EMAIL and ATLASSIAN_API_TOKEN (see docs/SETUP_GUIDE.md). Demo stories still work.</p>}</div>
  <div className="panel"><h2>Stories</h2><table><tbody>{s.map(x => <tr key={x.story_id}>
    <td><b>{x.story_id}</b></td><td>{x.title}</td><td><Chip v={x.status} /></td>
    <td>{x.questions.filter(q => q.status === "awaiting_review").length} open questions</td>
    <td><button className="act" onClick={() => open(x.story_id)}>Open</button></td></tr>)}</tbody></table></div></>;
}
function Story({ sid, setErr }) {
  const [r, setR] = useState(null), [busy, setBusy] = useState(false), [ans, setAns] = useState({});
  const load = useCallback(() => api("/stories/" + sid).then(setR).catch(e => setErr(e.message)), [sid]);
  useEffect(() => { setR(null); load(); }, [load]);
  const run = async fn => { setBusy(true); setErr(""); try { await fn(); await load(); } catch (e) { setErr(e.message); } setBusy(false); };
  if (!r) return <p>Loading…</p>; const D = r.source_docs;
  return <>
    <div className="panel"><div className="row"><div><h2>{r.story_id}: {r.title}</h2><p>{r.description}</p></div><Chip v={r.status} /></div>
      <ul>{r.acceptance_criteria.map(a => <li key={a.id}><b>{a.id}</b> {a.text}</li>)}</ul>
      {r.import_warnings?.map((w, i) => <div className="err" key={i}>{w}</div>)}
      <p className="note">Sources loaded: {r.source_ids.map(s => `${s} ${D[s].name}`).join(", ")}. Each source shows its origin: demo fixture or live Atlassian import.</p>
      <button className="act" disabled={busy} onClick={() => run(() => post(`/stories/${sid}/analyze`))}>{busy ? "Working…" : "Analyze story"}</button></div>
    {r.analysis_stats && <>
      <div className="panel"><h2>Gaps and contradictions</h2>
        {!r.findings.length && <p>No gaps detected in the supplied sources.</p>}
        {r.findings.map(f => <div key={f.finding_id} style={{ marginBottom: "1rem" }}>
          <div className="row"><b>{f.finding_id} · {f.statement}</b><span><Chip v={f.severity} /> <Chip v={f.label} /> <Chip v={f.review_status} /></span></div>
          <p>{f.reasoning_summary} <span className="note">Confidence: {f.confidence}</span></p><Ev list={f.evidence} docs={D} /></div>)}</div>
      <div className="panel"><h2>Clarification questions</h2>
        {!r.questions.length && <p>No questions needed.</p>}
        {r.questions.map(q => <div key={q.question_id} style={{ marginBottom: ".8rem" }}>
          <div className="row"><span>{q.text}</span><Chip v={q.status} /></div>
          {q.status === "awaiting_review" && <><input aria-label="Answer from product owner (optional)" placeholder="Answer from product owner (optional, saved as a user-entered decision)" value={ans[q.question_id] || ""} onChange={e => setAns({ ...ans, [q.question_id]: e.target.value })} />
            <button className="act" onClick={() => run(() => post(`/stories/${sid}/review/questions/${q.question_id}`, { decision: "approved", response: ans[q.question_id] }))}>Approve (simulated send)</button>{" "}
            <button className="act alt" onClick={() => run(() => post(`/stories/${sid}/review/questions/${q.question_id}`, { decision: "rejected" }))}>Reject</button></>}</div>)}
        <p className="note">Approval is simulated: no message is sent anywhere.</p></div>
      <div className="panel"><h2>Traceability</h2><table><thead><tr><th>Criterion</th><th>Status</th><th>Evidence</th></tr></thead><tbody>
        {r.trace.map(t => <tr key={t.ac_id}><td><b>{t.ac_id}</b> {r.acceptance_criteria.find(a => a.id === t.ac_id)?.text}</td><td><Chip v={t.status} /></td>
          <td>{t.evidence.length ? <Ev list={t.evidence} docs={D} /> : <span className="note">None supplied. This does not prove the code is missing.</span>}</td></tr>)}</tbody></table></div>
      <div className="panel"><div className="row"><h2>Documentation draft</h2>
        <button className="act" disabled={busy} onClick={() => run(() => post(`/stories/${sid}/docs`))}>{r.docs ? "Regenerate draft" : "Generate draft"}</button></div>
        {r.docs && <><div className="row"><Chip v={r.docs.status} />{r.docs.status === "awaiting_review" && <span>
          <button className="act" onClick={() => run(() => post(`/stories/${sid}/review/docs/docs`, { decision: "approved" }))}>Approve</button>{" "}
          <button className="act alt" onClick={() => run(() => post(`/stories/${sid}/review/docs/docs`, { decision: "rejected" }))}>Reject</button></span>}
          <a href={`/api/stories/${sid}/docs.md`} download={`${sid}.md`}>Export Markdown</a></div><pre>{r.docs.markdown}</pre></>}</div></>}
    <div className="panel"><h2>Audit trail</h2>{r.audit_events.length ? <table><tbody>{[...r.audit_events].reverse().map((a, i) => <tr key={i}><td>{a.at}</td><td>{a.event}</td><td>{a.item || a.mode || ""}</td></tr>)}</tbody></table> : <p className="note">No events yet. Analyze the story to begin.</p>}</div></>;
}
function Queue({ setErr, open }) {
  const [q, setQ] = useState([]); useEffect(() => { api("/queue").then(setQ).catch(e => setErr(e.message)); }, []);
  return <div className="panel"><h2>Awaiting review</h2>{!q.length && <p>Nothing to review. Analyze a story to generate questions or documentation.</p>}
    <table><tbody>{q.map(i => <tr key={i.story_id + i.id}><td>{i.story_id}</td><td>{i.kind}</td><td>{i.text}</td><td><button className="act" onClick={() => open(i.story_id)}>Review</button></td></tr>)}</tbody></table></div>;
}
function Eval({ setErr }) {
  const [e, setE] = useState(null); useEffect(() => { api("/eval").then(setE).catch(x => setErr(x.message)); }, []);
  if (!e) return <p>Loading…</p>; const pc = v => v == null ? "n/a" : Math.round(v * 100) + "%";
  return <div className="panel"><h2>Evaluation on seeded stories</h2>
    {!e.rows.length ? <p>Analyze at least one story to see results.</p> : <>
      <p>Gap precision <b>{pc(e.precision)}</b> · recall <b>{pc(e.recall)}</b> · evidence validity <b>{pc(e.evidence_validity)}</b></p>
      <table><thead><tr><th>Story</th><th>Seeded gaps</th><th>Detected</th><th>Seconds</th><th>Mode</th></tr></thead><tbody>
        {e.rows.map(r => <tr key={r.story_id}><td>{r.story_id}</td><td>{r.gold.join(", ") || "none"}</td><td>{r.detected.join(", ") || "none"}</td><td>{r.seconds}</td><td>{r.mode}</td></tr>)}</tbody></table></>}
    <p className="note">{e.note} Offline mode scores cached outputs, so only gemini-live runs measure the model. Compare time against a manual baseline you measure yourself.</p></div>;
}
