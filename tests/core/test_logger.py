import logging
from app.core.logger import logger


def test_logger():
    assert isinstance(logger, logging.Logger)
    logger.debug(logger.level)
    assert logger.level == logging.DEBUG
    assert logger.handlers[0].encoding == "utf-8"
    assert (
        logger.handlers[0].formatter._fmt
        == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    assert logger.handlers[0].formatter.datefmt == "%m/%d/%Y %I:%M:%S %p"
