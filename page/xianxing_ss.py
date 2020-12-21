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


            self.driver.find_element(By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(1)").click() #登录
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input").send_keys("dengchunwei") #用户名
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys("dcwkk520")  #密码
            self.driver.find_element(By.CSS_SELECTOR, "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input.us_Submit").click()  #登录
            sleep(5)

            #搜索
            self.driver.find_element(By.CSS_SELECTOR,"#keyword").send_keys("兰博基尼") #输入框
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,"#searchForm > span.ipt2 > input").click()#搜索按钮
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,"#compareForm > div > div:nth-child(1) > a > img").click() #点击图片

            self.driver.find_element(By.CSS_SELECTOR,"#ECS_FORMBUY > ul.bnt_ul > li.padd > a > img").click() #点击购买按钮
            sleep(2)

            self.driver.find_element(By.CSS_SELECTOR,"body > div.block.table > div.flowBox > table > tbody > tr > td:nth-child(2) > a > img").click() #点击结算中心
            sleep(2)

            # locator = self.driver.find_element(By.CSS_SELECTOR,"#selCountries_0")
            # select = Select(locator)
            # select.select_by_index(1)   #配送区域
            # sleep(2)
            # locator = self.driver.find_element(By.CSS_SELECTOR,"#selProvinces_0") #配送区域
            # select = Select(locator)
            # select.select_by_index(1)
            # sleep(2)
            # locator = self.driver.find_element(By.CSS_SELECTOR, "#selCities_0") #配送区域
            # select = Select(locator)
            # select.select_by_index(1)
            # sleep(3)
            # locator = self.driver.find_element(By.CSS_SELECTOR, "#selDistricts_0") #配送区域
            # select = Select(locator)
            # select.select_by_index(1)
            # self.driver.find_element(By.CSS_SELECTOR,"#consignee_0").send_keys("邓纯伟")      #收货姓名
            # sleep(2)
            # self.driver.find_element(By.CSS_SELECTOR, "#address_0").send_keys("成都市龙泉驿区")     #详细地址
            # sleep(2)
            # self.driver.find_element(By.CSS_SELECTOR, "#tel_0").send_keys("18981859435")     #电话
            # sleep(2)
            # self.driver.find_element(By.CSS_SELECTOR, "#email_0").clear().send_keys("945057717@qq.com")     #电子邮件地址
            # sleep(2)
            # self.driver.find_element(By.CSS_SELECTOR, "#theForm > div > table > tbody > tr:nth-child(6) > td > input.bnt_blue_2").click()     #点击配送到这个地址
            # sleep(2)

            self.driver.find_element(By.CSS_SELECTOR,"#shippingTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]").click()  #点击配送方式
            self.driver.find_element(By.CSS_SELECTOR,"#paymentTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]").click()  #点击支付方式
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,"#theForm > div:nth-child(12) > div:nth-child(3) > input[type=image]:nth-child(1)").click() #点击提交订单
            sleep(2)



        def tearDown(self):
            self.driver.quit()


    except NameError as e:
        print(e)


if __name__ == '__main__':
    unittest.main()