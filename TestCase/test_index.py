import sys
sys.path.append("../")#这句语句需要放在from语句之前，否则使用命令行运行pytest会报NotFound异常
from Page.PageSystem.UserPage import UserPage
from Page.LoginPage import LoginPage



class TestIndex:

    def setup_class(self):
        #调用Testlogin中
        self.user:UserPage = LoginPage().login_sucss_switch(UserPage)

    def teardown_class(self):
        self.user.close()


    #实现成功登录跳转至User页面
    def test_index_open_user(self):
        self.user.open_user_page()

