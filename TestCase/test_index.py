import sys
from Page.config import BaseConfig
sys.path.append("../")
from Page.LoginPage import LoginPage



class TestIndex:
    def setup_class(self):
        self.index = LoginPage().login_sucss(BaseConfig.loginuser,BaseConfig.loginpwd)


    def teardown_class(self):
        # self.login.driver.switch_to.window(self.login.driver.window_handles[0])
        self.index.close()

    def test_index_open_userpage(self):
        self.index.open_user_page()
