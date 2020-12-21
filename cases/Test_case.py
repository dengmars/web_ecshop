
from model.Broswer_model import BroswerModel
from page.Login_page import LoginPage
from model.Read_page import ReadExcel
from page.Register_page import RegisterPage
from page.Userinfo_page import UserinfPage
from page.ReceiverAddress_page import AddressPage
from page.Home_page import HomePage
from page.Center_page import CenterPage
from page.login1_page import login1page
from page.home11_page import HomePage



from time import sleep
import unittest


class MyTest(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.driver = BroswerModel().broswer_chrome()

    def test_a(self):
    #     '''
    #     调用注册页面的方法和传入参数
    #     :return:
    #     '''
    #     lp = LoginPage(self.driver)
    #     lp.open()
    #     username, email, password, passwd, msn, qq, officephone, hometelephone, phone, encrypted_answern = ReadExcel("login")
    #     print(officephone)
    #     lp.login(username, email, password, passwd, msn, qq, officephone, hometelephone, phone, encrypted_answern)
    #
    #     # 调用用户信息页面的方法并传入数据
    #     up = UserinfPage(self.driver)
    #     officephone= ReadExcel("userinfo")
    #     print(officephone)
    #     up.userinfo(officephone)
    #     #调用收货地址页面的方法并传入数据
    #     rap = AddressPage(self.driver)
    #     consignee, detailedaddress, phone, email = ReadExcel("address")
    #     sleep(2)
    #     rap.address(consignee, detailedaddress, phone, email)
    #
    #     #断言
    #
    #     expected='小油油'
    #     actual=self.driver.find_element_by_id("consignee_0").get_attribute("value")
    #     print(actual)
    #     self.assertEqual(expected,actual,msg='新增地址失败')
    #     sleep(6)
    #
    #
    # def test_b(self):
    #     '''
    #     调用登录页面的方法并传入数据
    #     :return:
    #     '''
    #     rp=RegisterPage(self.driver)
    #     rp.open()
    #     username,password=ReadExcel("register")
    #     rp.register(username,password)
    #     sleep(2)
    #     #调用首页的方法
    #     hp=HomePage(self.driver)
    #     keyword=ReadExcel("home")
    #     hp.home(keyword)
    #     sleep(2)
    #     #断言
    #     cp=CenterPage(self.driver)
    #     cp.center()
    #     expected ="http://192.168.1.134:8080/upload/flow.php?step=done"
    #     actual=self.driver.current_url
    #     self.assertEqual(expected,actual,msg="生成订单不成功")



        

        self.driver=BroswerModel().broswer_chrome()


        lp1=login1page(self.driver)
        lp1.open()
        #login1page(self.driver).open()
        #Home1Page(self.driver).open()
        username,password=ReadExcel("login1")
        lp1.login(username,password)


        hp1=HomePage(self.driver)
        hp1.Menu()











    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
