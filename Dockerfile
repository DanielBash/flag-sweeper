FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENV RUN_MODE=production

CMD ["gunicorn", "--config", "gunicorn_config.py", "main:app"]