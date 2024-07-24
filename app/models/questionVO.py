class QuestionVO:
    def __init__(self, question_id, question_text, interview_id):
        self.question_id = question_id
        self.question_text = question_text
        self.interview_id = interview_id

    def __repr__(self):
        return f"<QuestionVO(question_id={self.question_id}, interview_id={self.interview_id})>"
