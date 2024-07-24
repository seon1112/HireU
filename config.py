import os

#SQLAlchemy 설정
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/hireu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 객체 변경 사항 추적 비활성화