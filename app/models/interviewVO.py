from datetime import datetime

class InterviewVO:
    def __init__(self, interview_id, interview_nm, user_id, created_at=None, updated_at=None):
        self.interview_id = interview_id
        self.interview_nm = interview_nm
        self.user_id = user_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return f"<InterviewVO(interview_id={self.interview_id}, interview_nm={self.interview_nm})>"
