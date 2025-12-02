# -------- Step 1: Build React Frontend --------
FROM node:18 AS frontend-build
WORKDIR /app/frontend

COPY frontend/package.json .
RUN npm install

COPY frontend/ .
RUN npm run build


# -------- Step 2: Build Flask Backend --------
FROM python:3.10

COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend /app

# Copy React build → Flask static folder
COPY --from=frontend-build /app/frontend/build /app/static

WORKDIR /app

EXPOSE 7860

CMD ["python", "app.py"]
