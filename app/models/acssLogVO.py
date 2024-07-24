from datetime import datetime

class AcssLogVO:
    def __init__(self, acss_log_num, user_id, acss_ip, log_txt, acss_at=None):
        self.acss_log_num = acss_log_num
        self.user_id = user_id
        self.acss_ip = acss_ip
        self.log_txt = log_txt
        self.acss_at = acss_at or datetime.now()

    def __repr__(self):
        return f"<AcssLogVO(acss_log_num={self.acss_log_num}, user_id={self.user_id})>"
