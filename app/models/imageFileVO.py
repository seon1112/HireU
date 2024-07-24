from datetime import datetime

class ImageFileVO:
    def __init__(self, file_seq, org_file_nm, sys_file_nm, file_path, reg_id, reg_dt=None, down_num=0):
        self.file_seq = file_seq
        self.org_file_nm = org_file_nm
        self.sys_file_nm = sys_file_nm
        self.file_path = file_path
        self.reg_id = reg_id
        self.reg_dt = reg_dt or datetime.now()
        self.down_num = down_num

    def __repr__(self):
        return f"<ImageFileVO(file_seq={self.file_seq}, org_file_nm={self.org_file_nm})>"
