from selenium.webdriver.common.by import By
from page.Base_page import BasePage
from time import sleep
class Home1Page(BasePage):

    member_locator=(By.CSS_SELECTOR,"#menu-ul > li.collapse.lis.ico_1")
    lst_locator=(By.CSS_SELECTOR,"#menu-ul > li.explode.lis.ico2_1 > ul > li:nth-child(1) > a")

    examine_locator=(By.CSS_SELECTOR,"#listDiv > table > tbody > tr:nth-child(3) > td:nth-child(10) > a:nth-child(3) > img")
    def input_farme1(self):
        self.driver.switch_to.frame("#menu-frame")

    def input_member(self):
        self.find_element(self.member_locator).click()

    def input_lst(self):
        self.find_element(self.lst_locator).click()
    def input_farme2(self):
        self.driver.switch_to.parent_frame()
    def input_farme3(self):
        self.driver.switch_to.frame("#main-frame")
    def input_examine(self):
        self.find_element(self.examine_locator).click()
    # def open(self):
    #     self.driver.get(self.url)
    def login1(self):
        self.input_farme1()
        sleep(2)
        self.input_member()
        sleep(2)
        self.input_lst()
        sleep(2)
        self.input_farme2()
        self.input_farme3()
        sleep(2)
        self.input_examine()




