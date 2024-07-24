from datetime import datetime

class ErrorLogVO:
    def __init__(self, error_log_num, user_id, error_ip, error_url, error_txt, error_at=None):
        self.error_log_num = error_log_num
        self.user_id = user_id
        self.error_ip = error_ip
        self.error_url = error_url
        self.error_txt = error_txt
        self.error_at = error_at or datetime.now()

    def __repr__(self):
        return f"<ErrorLogVO(error_log_num={self.error_log_num}, user_id={self.user_id})>"
