import sys
sys.path.append("../")
import pytest
from Page.config import BaseConfig
import allure
from Page.LoginPage import LoginPage
from time import sleep


@allure.feature("登录页面")
class TestLogin:
    # 所有方法执行之前
    def setup_class(self):
        self.login = LoginPage()


    #所有方法执行之后
    def teardown_class(self):
        self.login.close()


    #每个方法后执行
    def teardown(self):
        sleep(0.2)

    #错误密码登录
    @allure.story("登录功能")
    @allure.title("错误密码登录")
    def test_login_error_pwd(self):
        error_message = self.login.login_error("143637","12345786")
        assert error_message=="帐号密码错误"


    # 错误账号登录
    @allure.story("登录功能")
    @allure.title("错误账号登录")
    def test_login_error_user(self):
        error_message = self.login.login_error("12345","123456")
        assert error_message == "用户不存在"

    #空密码登录登录
    @allure.story("登录功能")
    @allure.title("空密码登录登录")
    def test_login_null_pwd(self):
        error_message = self.login.login_pwd_null("143637", " ")
        assert error_message == "请输入登录密码，且长度不小于5位"

    # 空账号登录
    @allure.story("登录功能")
    @allure.title("空账号登录")
    def test_login_null_user(self):
        error_message = self.login.login_user_null(" ", "1234567")
        assert error_message == "请输入登录名，且长度不小于5位"

    #正确登录跳转至首页
    # @allure.story("登录功能")
    # @allure.title("正确登录跳转至index页面")
    # def test_login_sucss(self):
    #     #登录成功后跳至首页
    #     self.login.login_sucss(BaseConfig.LOGINUSER,BaseConfig.LOGINPWD)


    #成功登录后点击[退出]
    @allure.story("退出功能")
    @allure.title("正确登录后点击[退出]按钮")
    def test_login_quit(self):
        msg = self.login.login_sucss_quit()
        assert msg == "退出成功"

















