import logging
from pathlib import Path
from .utils import ensure_folder

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
ensure_folder(str(LOG_DIR))


def get_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        fh = logging.FileHandler(LOG_DIR / "app.log")
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    logger.setLevel(level)
    return logger
