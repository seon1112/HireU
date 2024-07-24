from datetime import datetime

class UserVO:
    def __init__(self, user_id, email, name=None, refresh_token=None, industry=None, job_position=None, technical_skills=None, major=None, certifications=None, special_experience=None, cover_letter=None, created_at=None, updated_at=None):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.refresh_token = refresh_token
        self.industry = industry
        self.job_position = job_position
        self.technical_skills = technical_skills
        self.major = major
        self.certifications = certifications
        self.special_experience = special_experience
        self.cover_letter = cover_letter
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    def __repr__(self):
        return f"<UserVO(user_id={self.user_id}, email={self.email})>"
