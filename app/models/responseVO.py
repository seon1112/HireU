class ResponseVO:
    def __init__(self, response_id, interview_id, question_id, response_text):
        self.response_id = response_id
        self.interview_id = interview_id
        self.question_id = question_id
        self.response_text = response_text

    def __repr__(self):
        return f"<ResponseVO(response_id={self.response_id}, interview_id={self.interview_id}, question_id={self.question_id})>"
