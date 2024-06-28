import logging


logger = logging.getLogger()
logging.basicConfig(
    filename="app_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
