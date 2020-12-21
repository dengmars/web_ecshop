
class BasePage():
    '''
    先定义一个页面的基类
    '''
    _url = "http://192.168.1.134:8080/upload"  # 基类_url的存放地址

    def __init__(self, driver, url=None):
        self.driver = driver
        self.QTurl = "http://192.168.1.134:8080/upload/index.php"
        if not url:
            url = self._url
        self.url = url

    def open(self):
        self.driver.get(self.url)
    def openQt(self):
        self.driver.get(self.QTurl)

    def find_element(self,locator,element=None):
        '''
        查找元素，要求传入定位器，如果只传入定位器，整个浏览器找。
        如果传入定位器，并且传入一个元素对象，就在这个元素上再查找元素
        :param locator:
        :param element:
        :return:
        '''
        if element:
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


