from Page.BasePage import BasePage
from Page.PageSystem.UserPage import UserPage


class IndexPage(BasePage):
    _base_url='http://192.168.1.253/#/index'

    def open_user_page(self):
        self.driver.find_element_by_xpath('//*[@class="el-submenu__title"]').click()
        self.driver.find_element_by_xpath('//*[@id="scroll"]/div[1]/div/ul/div[5]/div/li/ul/li/ul/li').click()
        return UserPage(self.driver)


