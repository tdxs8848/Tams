from Page.BasePage import BasePage


class UserPage(BasePage):
    yamlfilename = r"C:\Users\John\PycharmProjects\Tams\Page\datas\PageSystem\UserPage.yml"
    UserElement = BasePage.loadYaml(None,yamlfilename)

    def open_user_page(self):
        self.driver.find_element_by_xpath('//*[@class="el-submenu__title"]').click()
        self.driver.find_element_by_xpath('//*[@id="scroll"]/div[1]/div/ul/div[5]/div/li/ul/li/ul/li').click()
        # return UserPage(self.driver)