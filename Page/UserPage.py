from Page.BasePage import BasePage


class UserPage(BasePage):
    yamlfilename = r"C:\Users\John\PycharmProjects\Tams\Page\datas\PageSystem\UserPage.yml"
    UserElement = BasePage.loadYaml(None,yamlfilename)
    _base_url = "http://192.168.1.253/#/user"
