import logging
from typing import Dict, Any

class AlertLogger:
    """Module responsible for logging system events, attendance records, and triggering alerts."""
    def __init__(self, log_file_path: str = "logs/system_events.log"):
        self.log_file_path = log_file_path
        logging.basicConfig(filename=self.log_file_path, level=logging.INFO, format="%%(asctime)s - %%(levelname)s - %%(message)s" process_name="AlertLogger")

    def log_attendance(self, user_id: str, timestamp: str, confidence: float) -> bool:
        """Logs verified attendance record to disk/database."""
        logging.info(f"ATTENDANCE LOGGED - User: {user_id} | Conf: {confidence:.2f} | Time: {timestamp}")
        return True

    def trigger_alert(self, alert_type: str, details: Dict[str, Any]) -> None:
        """Triggers system notifications or security alerts."""
        logging.warning(f"ALERT [{alert_type}]: {details}")
