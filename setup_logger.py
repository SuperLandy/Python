import logging
from colorlog import ColoredFormatter


def setup_logger():
    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter(
        "[%(asctime)s.%(msecs)03d] %(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'bold_purple',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red',
        }
    )

    logger = logging.getLogger('meow')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


logger = setup_logger()
logger.debug('woshitiancai')
logger.info('woshitiancai')
logger.warn('woshitiancai')
logger.error('woshitiancai')
