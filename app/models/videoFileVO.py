from datetime import datetime

class VideoFileVO:
    def __init__(self, video_seq, org_file_nm, sys_file_nm, file_path, reg_id, reg_dt=None):
        self.video_seq = video_seq
        self.org_file_nm = org_file_nm
        self.sys_file_nm = sys_file_nm
        self.file_path = file_path
        self.reg_id = reg_id
        self.reg_dt = reg_dt or datetime.now()

    def __repr__(self):
        return f"<VideoFileVO(video_seq={self.video_seq}, org_file_nm={self.org_file_nm})>"
