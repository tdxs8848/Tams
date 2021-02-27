import sys
import time

import allure
import pytest

sys.path.append("../")  # 这句语句需要放在from语句之前，否则使用命令行运行pytest会报NotFound异常

from Page.LoginPage import LoginPage
from Page.PageSystem.UserPage import UserPage


class TestUser:

    def setup_class(self):
        # 调用Testlogin中登录和转换项目的方法在config中进行配置
        self.user: UserPage = LoginPage().login_sucss_switch(UserPage)
        # 打开User页面
        self.user.open_user_page()

    def teardown(self):
        time.sleep(0.5)

    def teardown_class(self):
        self.user.close()

    @pytest.mark.parametrize("account,errormessage",
                             [['', '登录账号不能为空'],
                              ['1', '登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位'],
                              ['1111', '登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位'],
                              ['1111111111111111', '登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位'],
                              ['**---', '登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位']],
                             ids=['输入账号为空', '账号输入1位', '账号输入4位', '账号输入大于15位', '账号输入特殊字符'])
    @allure.title("添加账号页面输入错误的密码")
    @allure.story("新增功能")
    def test_add_account_erroraccount(self, account, errormessage):
        errorMsg = self.user.user_add_account_erroraccount(account, "123456", "selauto", "13424405192")
        assert errorMsg == errormessage

    @pytest.mark.parametrize("pwd",
                             [[''],
                              ['1'],
                              ['1111']],
                             ids=['登录密码为空', '密码长度输入1位', '密码长度输入4位'])
    @allure.title("添加账号页面输入错误的密码")
    @allure.story("新增功能")
    def test_add_account_errorpwd(self, pwd, ):
        errorMsg = self.user.user_add_account_errorpwd("selauto", pwd, "selauto", "13424405192")
        assert errorMsg == "登录密码不能为空，且长度不小于5位"

    @allure.title("添加账号页面输入空值姓名")
    @allure.story("新增功能")
    def test_add_account_nullname(self):
        errorMsg = self.user.user_add_account_nullname("selauto", "123456", "", "13424405192")
        assert errorMsg == "姓名不能为空"




    @pytest.mark.parametrize("phone,errormessage",
                             [['', '电话号不能为空，且长度为11位'],
                              ['23424405192', '电话号码格式不正确'],
                              ['1342440519', '电话号不能为空，且长度为11位'],
                              ['134244051922', '电话号不能为空，且长度为11位'],
                              ['1342440519陈', '电话号码格式不正确'],
                              ['1342440519a', '电话号码格式不正确'],
                              ['1342440519-', '电话号码格式不正确']],
                             ids=['电话号输入为空值', '电话号位首数字不为1', '电话号位数为10位', '电话号位数为12位', '电话号输入包含中文', '电话号输入包含英文',
                                  '电话号输入包含特殊符号'])
    @allure.title("添加账号页面输入错误的手机号")
    @allure.story("新增功能")
    def test_add_account_errorphone(self, phone, errormessage):
        errorMsg = self.user.user_add_account_errorphone("selauto", "123456", "selauto", phone)
        assert errorMsg == errormessage

    @allure.title("编辑账号页面输入空的姓名")
    @allure.story("编辑功能")
    def test_edit_account_nullname(self):
        errorMsg = self.user.user_edit_account_errorname("", "13424405192")
        assert errorMsg == "姓名不能为空"



    @pytest.mark.parametrize("phone,errorMessage",
                             [['', '电话号不能为空，且长度为11位'],
                              ['23424405192', '电话号码格式不正确'],
                              ['1342440519', '电话号不能为空，且长度为11位'],
                              ['134244051922', '电话号不能为空，且长度为11位'],
                              ['1342440519陈', '电话号码格式不正确'],
                              ['1342440519a', '电话号码格式不正确'],
                              ['1342440519-', '电话号码格式不正确']],
                             ids=['电话号输入为空值', '电话号位首数字不为1', '电话号位数为10位', '电话号位数为12位', '电话号输入包含中文', '电话号输入包含英文',
                                  '电话号输入包含特殊符号'])
    @allure.title("编辑账号页面输入错误的手机号")
    @allure.story("编辑功能")
    def test_edit_account_errorphont(self, phone, errorMessage):
        errorMsg = self.user.user_edit_account_errorphone("selauto",phone)
        assert errorMsg == errorMessage

    def test_add_account_sucss(self):
        # 使用月日与时间创建的字符串作为新增的用户名
        accountname = time.strftime("%m%d%H%M", time.localtime())
        self.user.user_add_account_sucss(accountname, "123456", "selauto", "13424405192")
