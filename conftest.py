import os
import logging
import pytest

# ლოგების საქაღალდის შექმნა, თუ არ არსებობს
os.makedirs("logs", exist_ok=True)

# ლოგირების ძირითადი კონფიგურაცია
logging.basicConfig(
    filename="logs/test_run.log",
    filemode="w",  # ყოველი გაშვებისას თავიდან იწერება
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@pytest.fixture(autouse=True)
def log_test_status(request):
    """ავტომატურად ასრულებს ლოგირებას თითოეული ტესტის დაწყების და დასრულებისას"""
    logging.info(f"--- ტესტი დაიწყო: {request.node.name} ---")
    yield
    logging.info(f"--- ტესტი დასრულდა: {request.node.name} ---\n")