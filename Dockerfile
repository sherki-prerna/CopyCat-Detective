# # -------- Step 1: Build React Frontend --------
# FROM node:18 AS frontend-build
# WORKDIR /app/frontend

# COPY frontend/package.json .
# RUN npm install

# COPY frontend/ .
# RUN npm run build


# # -------- Step 2: Build Flask Backend --------
# FROM python:3.10

# COPY backend/requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r /app/requirements.txt

# COPY backend /app

# # Copy React build → Flask static folder
# COPY --from=frontend-build /app/frontend/build /app/static

# WORKDIR /app

# EXPOSE 7860

# CMD ["python", "app.py"]

# -------- Step 1: Build React Frontend --------
FROM node:18 AS frontend-build
WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install

COPY frontend/ .
RUN npm run build


# -------- Step 2: Build Flask Backend --------
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Preload the embedding model during image build so first request doesn't
# trigger a large runtime download that can fail/timeout on Spaces.
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Copy backend source
COPY backend/ .

# Copy React build into Flask static folder
COPY --from=frontend-build /app/frontend/build ./static

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--workers", "1", "--timeout", "180", "app:app"]
