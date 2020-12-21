
class BasePage():
    url="http://192.168.1.134:8080/upload"
    def __init__(self,driver):
        self.driver=driver
    def open(self):
        return self.driver.get(self.url)
    def find_element(self,locator):
        return self.driver.find_element(*locator)

