


def login():
    '''登录页面'''
    name = input('请输入您的用户名:')
    passwd = input('请输入您的密码:')
    if name == 'admin' and passwd == 'passwd':#判断是否是管理员
        print('欢迎管理员登录')
        admin()#跳转管理员页面
    elif name in user_dict and passwd == user_dict[name]['passwd']:
        # 检测用户名是否存在
        print(f'学生{name}登录成功')
        stu()#跳转学生页面
    else:
        print('您的用户名或密码不对')
