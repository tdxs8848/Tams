import sys
import pytest
from Page.IndexPage import IndexPage
sys.path.append("../")
from Page.LoginPage import LoginPage
from TestCase.test_1login import TestLogin


class TestIndex:
    def setup_class(self):
        self.index = IndexPage()

    def teardown_class(self):
        # self.login.driver.switch_to.window(self.login.driver.window_handles[0])
        self.index.close()

    def test_index_open_userpage(self):
        self.index.open_user_page()
