import sys
sys.path.append("../")
import pytest
from Page.config import BaseConfig
import allure
from Page.LoginPage import LoginPage
import time


@allure.feature("登录页面")
class TestLogin:
    index = None
    # 所有方法执行之前
    def setup_class(self):
        self.login = LoginPage()


    #所有方法执行之后
    def teardown_class(self):
        # self.login.driver.switch_to.window(self.login.driver.window_handles[0])
        self.login.close()


    #每个方法后执行
    def teardown(self):
        time.sleep(1)

    # #错误密码登录
    # @allure.story("登录功能")
    # @allure.title("错误密码登录")
    # def test_login_error_pwd(self):
    #     error_message = self.login.login_error("143637","12345786")
    #     assert error_message=="帐号密码错误"
    #
    #
    # #错误账号登录
    # @allure.story("登录功能")
    # @allure.title("错误账号登录")
    # def test_login_error_user(self):
    #     error_message = self.login.login_error("12345","123456")
    #     assert error_message == "用户不存在"
    #
    # #空密码登录登录
    # @allure.story("登录功能")
    # @allure.title("空密码登录登录")
    # def test_login_null_pwd(self):
    #     error_message = self.login.login_pwd_null("143637", " ")
    #     assert error_message == "请输入登录密码，且长度不小于5位"
    #
    # # 空账号登录
    # @allure.story("登录功能")
    # @allure.title("空账号登录")
    # def test_login_null_user(self):
    #     error_message = self.login.login_user_null(" ", "1234567")
    #     assert error_message == "请输入登录名，且长度不小于5位"

    #正确登录跳转至首页
    @allure.story("登录功能")
    @allure.title("正确登录跳转至user页面")
    def test_login_sucss(self):
        #登录成功后跳至首页
        index = self.login.login_sucss(BaseConfig.loginuser,BaseConfig.loginpwd)
        #首页打开账号管理页面
        # self.index.open_user_page()
        return index














