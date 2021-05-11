from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.editcustomer import EditCustomer


class TestEditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    userID = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen()

    def test_edit_customer(self, setup):
        self.log.info('***** Test Edit Customer *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.log.info('***** Manager Login *****')
        self.LP = LoginPage(self.driver)
        self.LP.setusername(self.userID)
        self.LP.setpassword(self.password)
        self.LP.clicklogin()
        self.log.info('***** Login Successful *****')

        self.log.info('***** Edit Customer Bio *****')
        self.EC = EditCustomer(self.driver)
        self.EC.click_edit_customer_menu()
        self.EC.set_customer_id('22384')
        self.EC.click_submit_customer_id()
        self.EC.edit_address('street food no 4')
        self.EC.edit_city('Forbidden City')
        self.EC.edit_state('Forbidden State')
        self.EC.edit_pin('654321')  # 6 digits only
        self.EC.edit_phone('3465856323890854')
        self.EC.edit_email('paponksayangmami@gmail.com')
        self.EC.click_submit_edit()
        self.log.info('***** Customer data have been saved *****')

        self.msg = self.driver.find_element_by_tag_name('body').text
        print(self.msg)
        if 'Customer details updated Successfully!!!' in self.msg:
            assert True is True
            self.log.info('***** Edit Customer bio was Success *****')
        else:
            self.driver.save_screenshot('./Screenshots/' + 'test_edit_customer.png')
            assert True is False
            self.log.error('*****Test Failed *****')

        self.driver.close()
        self.log.info('***** Test Finished *****')
