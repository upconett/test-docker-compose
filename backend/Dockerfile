FROM python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .

EXPOSE 8000

RUN uv sync
CMD uv run uvicorn --host 0.0.0.0 --port 8000 app:app
