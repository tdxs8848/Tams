import pytest
from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
import time

from Page.PageSystem.UserPage import UserPage
from Page.config import BaseConfig


class LoginPage(BasePage):
    _base_url = BaseConfig.URL

    # 定义登录方法
    def loginin(self, username, password):
        self.findElementXpathYml('name').clear()
        self.findElementXpathYml('pwd').clear()
        self.findElementXpathYml('name').send_keys(username)
        self.findElementXpathYml('pwd').send_keys(password)
        self.findElementXpathYml('loginBtn').click()
        time.sleep(2)

    # 成功登录
    def login_sucss(self, username, password):
        self.loginin(username, password)
        return UserPage(self.driver)

    # 错误登录
    def login_error(self, username, password):
        self.loginin(username, password)
        # 获取警告信息
        time.sleep(0.5)
        tips_message = self.driver.find_element_by_xpath(self.PageElement.get('alert')).text
        return tips_message

    # 空密码登录
    def login_pwd_null(self, username, password):
        self.loginin(username, password)
        # 获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.PageElement.get("pwdInputMessage")).text
        return tips_message

    # 空账号登录
    def login_user_null(self, username, password):
        self.loginin(username, password)
        # 获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.PageElement.get("userInputMessage")).text
        return tips_message

    # 成功登录后点击[退出]按钮
    def login_sucss_quit(self):
        userPage = self.login_sucss(BaseConfig.LOGINUSER,BaseConfig.LOGINPWD)
        userPage.findElementXpathYml('quitBtn').click()
        return self.findElementXpathYml('quitMsg').get_attribute('textContent')


    def login_sucss_switch(self, pageObject: BasePage):
        '''
        实现登录跳转功能
        在其他页面依赖登录功能时，传入他们的页面对象后，对登录后的driver进行返回实现复用
        '''
        self.loginin(BaseConfig.LOGINUSER, BaseConfig.LOGINPWD)
        # 登录成功后切换自己的项目
        self.chang_project()
        return pageObject(self.driver)

    # 选择自己的项目
    def chang_project(self):
        self.driver.find_element_by_xpath(self.PageElement.get("topNavSelectPro")).click()
        select = self.driver.find_element_by_xpath(self.PageElement.get("topNavSelectProLi"))
        # 遍历获取框架下拉框的值
        project = select.find_elements_by_tag_name("li")
        for p in project:
            if p.find_element_by_tag_name("span").text.__contains__(BaseConfig.PROJECT):
                p.click()
                break
        time.sleep(1)
