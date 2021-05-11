
class DeleteCustomer:
    btnMenuDelCustomer_xpath = '/html/body/div[2]/div/ul/li[4]/a'
    txtCustomerID_name = 'cusid'
    btnSubmitID_name = 'AccSubmit'

    def __init__(self, driver):
        self.driver = driver

    def click_delete_customer(self):
        self.driver.find_element_by_xpath(self.btnMenuDelCustomer_xpath).click()

    def set_customer_id(self, id):
        self.driver.find_element_by_name(self.txtCustomerID_name).send_keys(id)

    def click_submit_id(self):
        self.driver.find_element_by_name(self.btnSubmitID_name).click()
