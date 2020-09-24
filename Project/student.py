import data_example
from FileSetting import save_data


def register():
    while True:
        name = input("请输入用户名：")
        psw = input("请输入密码：")
        if name in data_example.user_dict:
            print("用户名已存在，请更换")
            continue
        if len(psw) < 6:
            print("密码长度不够")
            continue
        data_example.user_dict[name] = {"account": name, "passwd": psw}
        save_data(data_example.user_dict)
        print("注册成功")
        break
