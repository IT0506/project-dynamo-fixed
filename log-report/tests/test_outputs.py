import json
from pathlib import Path


def load_report():
    with open("/app/report.json", "r", encoding="utf-8") as f:
        return json.load(f)


def test_report_exists():
    """Success Criterion 1: The report is written to /app/report.json."""
    assert Path("/app/report.json").exists(), "report.json was not created"


def test_report_is_valid_json():
    """Success Criterion 2: The report is valid JSON."""
    load_report()


def test_total_requests():
    """Success Criterion 3: total_requests equals the number of log entries."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 4: unique_ips equals the number of distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 5: top_path equals the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"