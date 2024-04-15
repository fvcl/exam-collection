from datetime import datetime

def format_date_info(severity="INFO"):
    return f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} +0000] [MAIN] [{severity}]"
