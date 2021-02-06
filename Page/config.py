class BaseConfig:
    #测试项目所在路径
    PROJECTPATH = "C:\\Users\\John\\PycharmProjects\\"
    #登录页面地址
    URL = 'http://192.168.1.253/#/'
    #正确登录账号
    LOGINUSER = 'super_admin'
    #正确登录密码
    LOGINPWD = 'admin'
    #所选项目
    PROJECT = "ctest"
    #当运行项目比较卡导致，大批量用例报错时，建议调大该数值，sleeptime是增加关键跳转位置的时间
    SLEEPTIME = 0.5

