import pytest
from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
import time
from Page.config import BaseConfig


class LoginPage(BasePage):
    yamlfilename = BaseConfig.PROJECTPATH+"Tams\\Page\\datas\\LoginPage.yml"
    LoginElement = BasePage.loadYaml(None,yamlfilename)
    _base_url = BaseConfig.URL



    #定义登录方法
    def loginin(self,username,password):
        #清空输入框的值
        self.driver.find_element(By.XPATH, self.LoginElement.get('name')).clear()
        self.driver.find_element(By.XPATH, self.LoginElement.get('pwd')).clear()
        #输入账号密码
        self.driver.find_element(By.XPATH, self.LoginElement.get('name')).send_keys(username)
        self.driver.find_element(By.XPATH, self.LoginElement.get('pwd')).send_keys(password)
        #点击登录
        self.driver.find_element(By.XPATH, self.LoginElement.get('loginBtn')).click()
        time.sleep(2)

    #成功登录
    def login_sucss(self,username,password):
        self.loginin(username,password)


    #错误登录
    def login_error(self,username,password):
        self.loginin(username,password)
        #获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.LoginElement.get('alert')).text
        return tips_message

    #空密码登录
    def login_pwd_null(self,username,password):
        self.loginin(username,password)
        #获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.LoginElement.get("pwdInputMessage")).text
        return tips_message

    #空账号登录
    def login_user_null(self, username, password):
        self.loginin(username, password)
        # 获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.LoginElement.get("userInputMessage")).text
        return tips_message



    def login_sucss_switch(self,pageObject:BasePage):
        '''
        实现登录跳转功能
        在其他页面依赖登录功能时，传入他们的页面对象后，对登录后的driver进行返回实现复用
        '''
        self.loginin(BaseConfig.LOGINUSER,BaseConfig.LOGINPWD)
        #登录成功后切换自己的项目
        self.chang_project()
        return pageObject(self.driver)


    #选择自己的项目
    def chang_project(self):
        self.driver.find_element_by_xpath(self.LoginElement.get("topNavSelectPro")).click()
        select = self.driver.find_element_by_xpath(self.LoginElement.get("topNavSelectProLi"))
        #遍历获取框架下拉框的值
        project = select.find_elements_by_tag_name("li")
        for p in project:
            if p.find_element_by_tag_name("span").text.__contains__(BaseConfig.PROJECT):
                p.click()
                break
        time.sleep(1)