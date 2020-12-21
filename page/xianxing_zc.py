import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MyTest(unittest.TestCase):
    try:
        driver = webdriver.Chrome()

        driver.get("http://192.168.1.134:8080/upload")
        driver.implicitly_wait(30)


        # shouye_locator=driver.find_element(By.CSS_SELECTOR,"body > div.menu_box.clearfix > div > div > a.cur").click()
        zhuce_locator=driver.find_element(By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(2)").click()  #点击注册
        username_locator=driver.find_element(By.CSS_SELECTOR,"#username").send_keys("dengchunwei") #输入用户名
        email_locator=driver.find_element(By.CSS_SELECTOR,"#email").send_keys("2514011123@qq.com")  #输入邮箱
        password_locator=driver.find_element(By.CSS_SELECTOR,"#password1").send_keys("dcwkk520")   #输入密码
        paswd_locator=driver.find_element(By.CSS_SELECTOR,"#conform_password").send_keys("dcwkk520")   #确认密码
        msn_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input").send_keys("2514011006@qq.com") #输入MSN
        qq_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input").send_keys("2514011006")  #输入qq
        officephone_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(8) > td:nth-child(2) > input").send_keys("8384848")  #输入办公电话
        hometelephone_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(9) > td:nth-child(2) > input").send_keys("6746723")  #输入家庭电话
        phone_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(10) > td:nth-child(2) > input").send_keys("18981859435")  #输入手机
        locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > select")   #选择密保问题
        select=Select(locator)
        select.select_by_index(1)
        daan_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > input").send_keys("战狼")   #输入密保答案
        submit_locator=driver.find_element(By.CSS_SELECTOR,"body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(14) > td:nth-child(2) > input.us_Submit_reg").click()   #点击注册



    except NameError as e:
        print(e)

if __name__=='__main__':
    unittest.main()

