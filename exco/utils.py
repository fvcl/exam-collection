from datetime import datetime

def format_date_info(severity="INFO"):
    """
    Formats a date info string with the current date and time. This is to make print messages look nicer when logging.
    """
    return f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} +0000] [MAIN] [{severity}]"
