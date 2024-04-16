from datetime import datetime
from abc import ABC, abstractmethod


def format_date_info(severity="INFO"):
    """
    Formats a date info string with the current date and time. This is to make print messages look nicer when logging.
    """
    return f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} +0000] [MAIN] [{severity}]"


def get_db_models():
    try:
        import exco.models as models
    except ImportError:
        import models
    classes_map = {}
    for name, obj in models.__dict__.items():
        if isinstance(obj, type):
            classes_map[name] = obj

    return classes_map


class Mockable(ABC):
    @abstractmethod
    def generate_mock_data(self):
        pass
