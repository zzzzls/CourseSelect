user_dict = {
    "zs": {"account": 'zs', "username": "张三", "passwd": "123456", "score": "1", "course": set()}
}

print("欢迎来到选课系统")
print("1-----用户注册")
print("2-----用户登录")
print("3-----退出")
a = input("请选择您要操作的序号")
while True:
    if a == "1":
        name = input("请输入用户名：")
        psw= input("请输入密码：")
        if name in user_dict:
            print("用户名已存在，请更换")
            continue
        if len(psw)<6:
            print("密码长度不够")
            continue
        user_dict[name]={"用户名":name,"密码":psw}
        print("注册成功")
        break