import sys
#这句语句需要放在from语句之前，否则使用命令行运行pytest会报NotFound异常
sys.path.append("../")
from Page.IndexPage import IndexPage
from Page.LoginPage import LoginPage



class TestIndex:

    def setup_class(self):
        self.index:IndexPage = LoginPage().login_sucss_switch(IndexPage)

    def teardown_class(self):
        self.index.close()


    #实现成功登录跳转至User页面
    def test_index_open_user(self):
        self.index.open_user_page()

