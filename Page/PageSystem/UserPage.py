import time


from Page.BasePage import BasePage
from Page.config import BaseConfig


class UserPage(BasePage):
    yamlfilename = BaseConfig.PROJECTPATH+"Tams\\Page\\datas\\PageSystem\\UserPage.yml"
    #如果要使用BaseDriver中的findElementXpathYml必须要赋值PageElement
    PageElement = BasePage.loadYaml(None,yamlfilename)


    def open_user_page(self):
        self.findElementXpathYml("systemSeting").click()
        self.findElementXpathYml("systemAccount").click()

    def user_add_account(self,account,pwd,name,phone):
        self.findElementXpathYml("addAccountBtn").click()
        #输入账号
        self.findElementXpathYml("accountInput").clear()
        self.findElementXpathYml("accountInput").send_keys(account)
        #输入密码
        self.findElementXpathYml("pwdInput").click()
        self.findElementXpathYml("pwdInput").send_keys(pwd)
        #输入姓名
        self.findElementXpathYml("nameInput").clear()
        self.findElementXpathYml("nameInput").send_keys(name)
        #输入电话
        self.findElementXpathYml("phontInput").clear()
        self.findElementXpathYml("phontInput").send_keys(phone)
        #选择项目管理员
        self.findElementXpathYml("roleRadio").click()
        #点击添加按钮
        self.findElementXpathYml("addBtn").click()

    def user_add_account_sucss(self,account,pwd,name,phone):
        self.user_add_account(account,pwd,name,phone)

    #输入错误的账号
    def user_add_account_erroraccount(self,account,pwd,name,phone):
        self.user_add_account(account, pwd, name, phone)
        #获取错误的账号报错信息
        errorMessage = self.findElementXpathYml("accountInputErrMsg").text
        #点击取消按钮
        self.findElementXpathYml("cancelBtn").click()
        return errorMessage

    #输入空密码
    def user_add_account_errorpwd(self,account,pwd,name,phone):
        self.user_add_account(account, pwd, name, phone)
        #获取空账号报错信息
        errorMessage = self.findElementXpathYml("pwdInputErrMsg").text
        #点击取消按钮
        self.findElementXpathYml("cancelBtn").click()
        return errorMessage

    #输入空姓名
    def user_add_account_nullname(self, account, pwd, name, phone):
        self.user_add_account(account, pwd, name, phone)
        # 获取空账号报错信息
        errorMessage = self.findElementXpathYml("nameInputErrMsg").text
        # 点击取消按钮
        self.findElementXpathYml("cancelBtn").click()
        return errorMessage

    #输入空电话
    def user_add_account_errorphone(self, account, pwd, name, phone):
        self.user_add_account(account, pwd, name, phone)
        # 获取空账号报错信息
        errorMessage = self.findElementXpathYml("phontInputErrMsg").text
        # 点击取消按钮
        self.findElementXpathYml("cancelBtn").click()
        return errorMessage
