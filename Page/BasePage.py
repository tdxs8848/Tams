import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class BasePage:
    def __init__(self,driver:WebDriver=None):
        print("正在初始化页面。。。")
        if driver is None:
            #打开浏览器
            self.driver =webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
            #设置隐式等待时间
            self.driver.implicitly_wait(5)
            #访问页面
            self.driver.get(self._base_url)
        else:
            self.driver = driver

#注意该位置多文件后是否会出现问题
    @staticmethod
    #读取yaml文件
    def loadYaml(filename):
        Data = yaml.load(open(filename, encoding='utf-8'),Loader=yaml.FullLoader)
        return Data


    # def findElementXpath(self,ymlName):
    #     self.driver.find_element_by_xpath(self.Data.get(ymlName))

    def close(self):
        print("十秒后关闭浏览器。。。")
        #强制等待十秒后关闭浏览器
        time.sleep(10)
        self.driver.close()





class TestC():
    def setup(self):
        print("start")
    def teardown(self):
        print("end")
    @pytest.mark.parametrize("data",[1,2,3,4,5,6,7,8,9,10])
    def test1(self,data):
        print(data)
