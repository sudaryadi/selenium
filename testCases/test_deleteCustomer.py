from selenium.webdriver.common.keys import Keys
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.deleteCustomer import DeleteCustomer
from time import sleep


class TestDeleteCustomer:

    baseURL = ReadConfig.getApplicationURL()
    userID = ReadConfig.getUseremail()
    userPass = ReadConfig.getPassword()
    log = LogGen.loggen()

    def test_delete_customer(self, setup):
        self.log.info('***** Test Delete Customer is Starting *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.log.info('***** Manager Login *****')
        self.LP = LoginPage(self.driver)
        self.LP.setusername(self.userID)
        self.LP.setpassword(self.userPass)
        self.LP.clicklogin()
        self.log.info('***** Login Successful *****')

        self.log.info('***** Cek user ID *****')
        self.DC = DeleteCustomer(self.driver)
        self.DC.click_delete_customer()
        self.DC.set_customer_id('63597')
        self.DC.click_submit_id()
        sleep(4)
        # self.driver.find_element_by_name("AccSubmit").send_keys(Keys.ENTER)

        self.msg = self.driver.find_element_by_tag_name('body').text
        print(self.msg)
        if 'You are not authorize to delete this customer!!' in self.msg:
            assert True is True
            self.log.info('***** Edit Customer bio was Success *****')
        else:
            self.driver.save_screenshot('./Screenshots/' + 'test_delete_customer.png')
            assert True is False
            self.log.error('*****Test Failed *****')

        self.driver.close()
        self.log.info('***** Test Finished *****')
