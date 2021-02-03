from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
import yaml
import time
from Page.IndexPage import IndexPage


class LoginPage(BasePage):

    yamlfilename = r"C:\Users\TdXs\PycharmProjects\Tams\Page\LoginPage.yml"
    # LoginData = yaml.load(open(r"C:\Users\TdXs\PycharmProjects\Tams\Page\LoginPage.yml",encoding='utf-8'))
    LoginData = BasePage.loadYaml(yamlfilename)
    _base_url = LoginData.get('base_url')
    # _base_url = 'http://192.168.1.253/#/'
    # _name = '//*[@class="el-input__inner"]'
    # _pwd = '//*[@id="app"]/div/div/form/div[2]/div/div/input'
    # _loginBtn = '//*[@id="app"]/div/div/form/div[3]/div/button/span'


    #定义登录方法
    def loginin(self,username,password):
        #清空输入框的值
        self.driver.find_element(By.XPATH, self.LoginData.get('name')).clear()
        self.driver.find_element(By.XPATH, self.LoginData.get('pwd')).clear()
        #输入账号密码
        self.driver.find_element(By.XPATH, self.LoginData.get('name')).send_keys(username)
        self.driver.find_element(By.XPATH, self.LoginData.get('pwd')).send_keys(password)
        #点击登录
        self.driver.find_element(By.XPATH, self.LoginData.get('loginBtn')).click()

    #成功登录
    def login_sucss(self,username,password):
        self.loginin(username,password)
        return IndexPage(self.driver)

    #错误登录
    def login_error(self,username,password):
        self.loginin(username,password)
        time.sleep(2)
        #获取警告信息
        tips_message = self.driver.find_element_by_xpath(self.LoginData.get('alert')).text
        print("tips_massage:"+tips_message)
        return tips_message
    #
    # #空密码登录
    # def login_pwd_null(self,username,password):
    #     self.loginin(username,password)
    #     #获取警告信息
    #     tips_message = self.driver.find_element_by_xpath(self.LoginData.get("pwdInputMessage")).text
    #     print("tips_massage:" + tips_message)
    #     return tips_message
    #
    # #空账号登录
    # def login_user_null(self, username, password):
    #     self.loginin(username, password)
    #     # 获取警告信息
    #     # tips_message = self.driver.find_element_by_xpath(self.LoginData.get("userInputMessage")).text
    #     # tips_message = self.findElementXpath("userInputMessage")
    #     tips_message = self.driver.find_element_by_xpath(self.LoginData.get("userInputMessage")).text
    #
    #     print("tips_massage:" + tips_message)
    #     return tips_message

