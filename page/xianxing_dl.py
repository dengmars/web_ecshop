import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class MyTest(unittest.TestCase):
    try:

        driver = webdriver.Chrome()


        driver.get("http://192.168.1.134:8080/upload")
        driver.maximize_window()
        driver.implicitly_wait(30)
        def test_a(self):

            print(".......")
            self.driver.find_element(By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(1)").click()  #点击登录
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input").send_keys("dengchunwei") #输入用户名
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys("dcwkk520")  #输入密码
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input.us_Submit").click()  #点击登录按钮
            #断言
            self.expected = "dengchunwei"
            self.actual = self.driver.find_element(By.LINK_TEXT, "dengchunwei").text
            self.assertEqual(self.expected,self.actual,msg="登录失败")

            self.driver.find_element(By.CSS_SELECTOR,"body > div.top_nav > div > div > a:nth-child(4)").click() #点击我的账户
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,"body > div.block.clearfix > div.AreaL > div > div > div > div > a:nth-child(2)").click() #点击我的用户信息
            sleep(2)

            self.driver.find_element(By.CSS_SELECTOR,"body > div.block.clearfix > div.AreaR > div > div > div > form:nth-child(4) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input").clear() #清空办公电话
            self.driver.find_element(By.CSS_SELECTOR,
                                     "body > div.block.clearfix > div.AreaR > div > div > div > form:nth-child(4) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input").send_keys("8787979767") #输入办公电话
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,"body > div.block.clearfix > div.AreaR > div > div > div > form:nth-child(4) > table > tbody > tr:nth-child(11) > td > input.bnt_blue_1").click()  #点击确认修改

        def tearDown(self):
            self.driver.quit()


    except NameError as e:
        print(e)


if __name__ == '__main__':
    unittest.main()