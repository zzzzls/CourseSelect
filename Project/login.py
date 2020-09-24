import data_example

def login():
    '''登录页面'''
    name = input('请输入您的用户名:')
    passwd = input('请输入您的密码:')
    if name in data_example.user_dict and passwd == data_example.user_dict[name]['passwd']:
        # 检测用户名是否存在
        print(f'学生{name}登录成功')
    else:
        print('您的用户名或密码不对')
