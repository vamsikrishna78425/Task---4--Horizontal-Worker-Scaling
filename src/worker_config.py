"""
WORKER SCALING COMMAND REFERENCE
=================================

Method 1 — Multiple Workers:
    celery -A celery_app worker --loglevel=info -n worker1@%h
    celery -A celery_app worker --loglevel=info -n worker2@%h

Method 2 — Concurrency Flag:
    celery -A celery_app worker --concurrency=4 --loglevel=info

Method 3 — Autoscaling:
    celery -A celery_app worker --autoscale=10,3 --loglevel=info
"""

WORKER_CONFIGS = {
    "single":    {"concurrency": 1,  "throughput": "~10 tasks/sec"},
    "scaled_4":  {"concurrency": 4,  "throughput": "~40 tasks/sec"},
    "scaled_8":  {"concurrency": 8,  "throughput": "~80 tasks/sec"},
    "autoscale": {"min": 3, "max": 10, "throughput": "~30-100 tasks/sec"},
}

def get_config(mode: str) -> dict:
    return WORKER_CONFIGS.get(mode, {})
