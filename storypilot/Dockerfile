FROM node:20-slim AS ui
WORKDIR /ui
COPY frontend/ .
RUN npm install && npm run build
FROM python:3.12-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app app
COPY --from=ui /ui/dist static
ENV PORT=8080
CMD exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
