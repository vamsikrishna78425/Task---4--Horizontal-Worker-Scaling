#  Horizontal Worker Scaling

**Module:** Celery Module  
**Intern:** Vamsi Krishna Darla  
**Supervisor:** Vasudha Tayade | **Captain:** Ayesha Faquih  

---

## Overview

Study of Horizontal Worker Scaling using Celery — how adding more workers increases task throughput in distributed task queue systems.

---

## Project Structure

- `src/celery_app.py` — Celery app and sample task  
- `src/worker_config.py` — Scaling configs and command reference  
- `tests/test_workers.py` — Unit tests  
- `requirements.txt` — Dependencies  
- `README.md` — Documentation  

---

## Setup & Run

Install dependencies:
`pip install -r requirements.txt`

Start a single worker:
`celery -A src.celery_app worker --loglevel=info`

Scale with concurrency:
`celery -A src.celery_app worker --concurrency=4 --loglevel=info`

Autoscaling:
`celery -A src.celery_app worker --autoscale=10,3 --loglevel=info`

Run tests:
`pytest tests/`

---

## Throughput Reference

| Workers | Throughput | Avg Latency |
|---------|-----------|-------------|
| 1 | ~10 tasks/sec | ~100ms |
| 2 | ~20 tasks/sec | ~50ms |
| 4 | ~40 tasks/sec | ~25ms |
| 8 | ~80 tasks/sec | ~12ms |

---

## Tech Stack

- Python
- Celery
- Redis
- Pytest

---

## Author

- **Intern:** Vamsi Krishna Darla  
- **Supervisor:** Vasudha Tayade  
- **Captain:** Ayesha Faquih  
- **Task:**  — Study Horizontal Worker Scaling
