
class EditCustomer:
    btnEditCustomer_xpath = '/html/body/div[2]/div/ul/li[3]/a'
    txtCustomerID_name = 'cusid'
    btnSubmitCustomerID_name = 'AccSubmit'

    # Only can edit some data
    txtEditAddress_name = 'addr'
    txtEditCity_name = 'city'
    txtEditState_name = 'state'
    txtEditPIN_name = 'pinno'
    txtEditPhone_name = 'telephoneno'
    txtEditEmail_name = 'emailid'
    btnSaveEditCustomer_name = 'sub'

    def __init__(self, driver):
        self.driver = driver

    def click_edit_customer_menu(self):
        self.driver.find_element_by_xpath(self.btnEditCustomer_xpath).click()

    def set_customer_id(self, custid):
        self.driver.find_element_by_name(self.txtCustomerID_name).send_keys(custid)

    def click_submit_customer_id(self):
        self.driver.find_element_by_name(self.btnSubmitCustomerID_name).click()

    def edit_address(self, address):
        self.driver.find_element_by_name(self.txtEditAddress_name).clear()
        self.driver.find_element_by_name(self.txtEditAddress_name).send_keys(address)

    def edit_city(self, city):
        self.driver.find_element_by_name(self.txtEditCity_name).clear()
        self.driver.find_element_by_name(self.txtEditCity_name).send_keys(city)

    def edit_state(self, state):
        self.driver.find_element_by_name(self.txtEditState_name).clear()
        self.driver.find_element_by_name(self.txtEditState_name).send_keys(state)

    def edit_pin(self, pin):
        self.driver.find_element_by_name(self.txtEditPIN_name).clear()
        self.driver.find_element_by_name(self.txtEditPIN_name).send_keys(pin)

    def edit_phone(self, phone):
        self.driver.find_element_by_name(self.txtEditPhone_name).clear()
        self.driver.find_element_by_name(self.txtEditPhone_name).send_keys(phone)

    def edit_email(self, email):
        self.driver.find_element_by_name(self.txtEditEmail_name).clear()
        self.driver.find_element_by_name(self.txtEditEmail_name).send_keys(email)

    def click_submit_edit(self):
        self.driver.find_element_by_name(self.btnSaveEditCustomer_name).click()
