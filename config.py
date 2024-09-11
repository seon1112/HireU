import os

#SQLAlchemy 설정
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/hireu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 객체 변경 사항 추적 비활성화
    CLIENT_ID = "23dec565a03973e95d013f68a68c6b98"
    CLIENT_SECRET = "j9EVejVYxRPSDu7lhhmniy9fCMbk1Vym"
    REDIRECT_URI = "http://localhost:5000/oauth"