from Page.LoginPage import LoginPage
import time

class TestLogin:
    # 所有方法执行之后
    def setup_class(self):
        self.login = LoginPage()

    #所有方法执行之后
    def teardown_class(self):
        # self.login.driver.switch_to.window(self.login.driver.window_handles[0])
        self.login.close()

    #每个方法后执行
    def teardown(self):
        time.sleep(3)

    #错误密码登录
    def test_login_error_pwd(self):
        error_message = self.login.login_error("143637","12345786")
        assert error_message=="帐号密码错误"


    #错误账号登录
    def test_login_error_user(self):
        error_message = self.login.login_error("12345","123456")
        assert error_message == "用户不存在"

    #空密码登录登录
    def test_login_null_pwd(self):
        error_message = self.login.login_pwd_null("143637", "")
        assert error_message == "请输入登录密码，且长度不小于5位"

    # 空账号登录
    def test_login_null_user(self):
        error_message = self.login.login_user_null("", "123456")
        assert error_message == "请输入登录名，且长度不小于5位"

    #正确登录跳转至首页
    def test_login_sucss(self):
        self.login.login_sucss("143637","123456")

