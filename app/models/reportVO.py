from datetime import datetime

class ReportVO:
    def __init__(self, report_id, interview_id, question_id, morpheme, cloud_grap, face_image, smile, angry, sad, face_less, speaking_speed, video_seq, total_comment, created_at=None):
        self.report_id = report_id
        self.interview_id = interview_id
        self.question_id = question_id
        self.morpheme = morpheme
        self.cloud_grap = cloud_grap
        self.face_image = face_image
        self.smile = smile
        self.angry = angry
        self.sad = sad
        self.face_less = face_less
        self.speaking_speed = speaking_speed
        self.video_seq = video_seq
        self.total_comment = total_comment
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"<ReportVO(report_id={self.report_id}, interview_id={self.interview_id}, question_id={self.question_id})>"
