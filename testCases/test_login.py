from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLoginManager:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_dashboard_title(self, setup):
        self.logger.info("***************** Test Dashboard Title *********************")
        self.logger.info("***************** Verifying Dashboard Title *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Guru99 Bank Home Page":
            assert True
            self.logger.info("***************** Test result is passed *********************")
            self.driver.quit()
        else:
            self.driver.save_screenshot("./Screenshots/"+"test_dashboard_title.png")
            self.logger.error("***************** Test result is failed *********************")
            self.driver.quit()
            assert False

    def test_login_manager(self, setup):
        self.logger.info("***************** Test Login Manager *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        pswd = self.lp.setpassword(self.password)  # wrong password # failed test # get screenshot#
        if pswd:
            assert True
            self.logger.info("***************** Test result is passed *********************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login_manager.png")
            self.logger.error("***************** Test result is failed *********************")
            self.driver.close()
            assert False
        self.lp.clicklogin()

        act_title = self.driver.title
        self.driver.close()
        if act_title == "Guru99 Bank Manager HomePage":
            assert True
        else:
            assert False
