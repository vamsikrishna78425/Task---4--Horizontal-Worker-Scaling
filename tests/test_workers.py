import pytest
from src.worker_config import get_config, WORKER_CONFIGS


def test_single_worker_config():
    config = get_config("single")
    assert config["concurrency"] == 1

def test_scaled_4_worker_config():
    config = get_config("scaled_4")
    assert config["concurrency"] == 4

def test_scaled_8_worker_config():
    config = get_config("scaled_8")
    assert config["concurrency"] == 8

def test_autoscale_bounds():
    config = get_config("autoscale")
    assert config["min"] == 3
    assert config["max"] == 10

def test_all_configs_have_throughput():
    for mode, config in WORKER_CONFIGS.items():
        assert "throughput" in config

def test_invalid_mode_returns_empty():
    assert get_config("unknown") == {}
