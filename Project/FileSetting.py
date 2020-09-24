import os
import json


def get_data():
    """取出数据"""
    # 判断文件是否存在
    if os.path.exists("./database"):
        with open("./database", 'r', encoding='utf-8') as f:
            user_dict = json.load(f)
        # 存在则取出文件并返回
        return user_dict
    # 不存在则返回空字典
    return {}


def save_data(user_dict):
    """存储数据"""
    with open("./database", 'w', encoding='utf-8') as f:
        json.dump(user_dict, f)
