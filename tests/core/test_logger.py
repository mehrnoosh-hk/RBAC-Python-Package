import logging
from app.core import logger


def test_logger():
    assert isinstance(logger.logger, logging.Logger)
    assert logger.logger.level == logging.DEBUG
    assert logger.logger.handlers[0].encoding == "utf-8"
    assert (
        logger.logger.handlers[0].formatter._fmt
        == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    assert logger.logger.handlers[0].formatter.datefmt == "%m/%d/%Y %I:%M:%S %p"
