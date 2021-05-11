import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.addNewCustomer import AddNewCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestAddNewCustomer:
    baseURL = ReadConfig.getApplicationURL()
    userID = ReadConfig.getUseremail()
    userPassword = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_add_new_cust(self, setup):
        self.logger.info('***** Test starting *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info('***** Browser opened successfully *****')
        time.sleep(3)

        self.logger.info('***** Login as Manager *****')
        self.LP = LoginPage(self.driver)
        self.LP.setusername(self.userID)
        self.LP.setpassword(self.userPassword)
        self.LP.clicklogin()
        self.logger.info('***** Manager login successfully *****')

        self.logger.info('***** Add new customer by Manager *****')
        self.NewCust = AddNewCustomer(self.driver)
        self.NewCust.click_new_customer_btn()
        time.sleep(3)
        self.logger.info('***** Filling customer biodata *****')
        self.NewCust.set_cust_name('Kurozuki Orochi')
        self.NewCust.set_gender('male')
        self.NewCust.set_birthdate('12/12/2012')  # MM/DD/YYYY
        self.NewCust.set_address('Takeshi Castle')
        self.NewCust.set_city('Kuri Town')
        self.NewCust.set_state('Wano Country')
        self.NewCust.set_pin('123456')
        self.NewCust.set_phone('123456789012345')
        self.NewCust.set_email('orochi2@mailinator.com')
        self.NewCust.set_password('12345orochi')
        self.NewCust.click_submit()
        self.logger.info('***** Saving new customer data *****')
        time.sleep(5)

        self.logger.info('***** Verifying successful notification page *****')
        self.msg = self.driver.find_element_by_tag_name('body').text

        print(self.msg)
        if 'Customer Registered Successfully!!!' in self.msg:
            assert True == True
            self.logger.info('***** New customer added successfully *****')
        else:
            self.driver.save_screenshot('../Screenshots/' + 'test_add_new_customer.png')
            self.logger.error('***** Failed to add new customer *****')
            assert True == False

        self.driver.close()
        self.logger.info('***** Test finished *****')
