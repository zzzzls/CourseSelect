"""程序运行入口"""
import data_example
from student import register
from login import login
from FileSetting import *

while True:
    # 加载数据
    data_example.user_dict = get_data()

    print(">>> 学生管理系统 <<<")
    print("1. 用户登录")
    print("2. 用户注册")
    print("3. 退出")
    choice = input("请输入你的选择: ")
    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        break
    else:
        print("没有这个选项")



















