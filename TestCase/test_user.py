import sys
import time

import pytest

sys.path.append("../")#这句语句需要放在from语句之前，否则使用命令行运行pytest会报NotFound异常

from Page.LoginPage import LoginPage
from Page.PageSystem.UserPage import UserPage





class TestUser:

    def setup_class(self):
        #调用Testlogin中登录和转换项目的方法在config中进行配置
        self.user:UserPage = LoginPage().login_sucss_switch(UserPage)
    def teardown(self):
        time.sleep(0.5)

    def teardown_class(self):
        self.user.close()

    #打开User页面
    def test_index_open_user(self):
        self.user.open_user_page()

    @pytest.mark.parametrize("account,errormessage",
                             [['','登录账号不能为空'],
                              ['1','登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位'],
                              ['1111111111111111','登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位'],
                              ['**---','登录账号可由大写字母、小写字母、数字组成，且长度不小于5位,不大于15位']])
    def test_add_account_erroraccount(self,account,errormessage):
        errorMsg = self.user.user_add_account_erroraccount(account,"123456","selauto","13424405192")
        assert errorMsg == errormessage


    @pytest.mark.parametrize("pwd,errormessage",
                             [['',"登录密码不能为空，且长度不小于5位"],
                              ['11',"登录密码不能为空，且长度不小于5位"]])
    def test_add_account_errorpwd(self,pwd,errormessage):
        errorMsg = self.user.user_add_account_errorpwd("selauto", pwd, "selauto", "13424405192")
        assert errorMsg == errormessage
    #
    def test_add_account_nullname(self):
        errorMsg = self.user.user_add_account_nullname("selauto", "123456", "", "13424405192")
        assert errorMsg == "姓名不能为空"
    #TODO:完成手机参数化
    def test_add_account_errorphone(self):
        errorMsg = self.user.user_add_account_errorphone("selauto", "123456", "selauto", "")
        assert errorMsg == "电话号不能为空，且长度为11位"

    def test_add_account_sucss(self):
        #使用月日与时间创建的字符串作为新增的用户名
        accountname = time.strftime("%m%d%H%M", time.localtime())
        self.user.user_add_account_sucss(accountname,"123456","selauto","13424405192")


