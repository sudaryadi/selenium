import time


class AddNewCustomer:
    # Manager Home Page
    btnAddNewCust_xpath = "/html/body/div[2]/div/ul/li[2]/a"

    # Add Customer Page
    txtCustName_name = "name"
    rdMale_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]"
    rdFemale_xpath = "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]"
    txtBirthdate_id = "dob"
    txtAddress_name = "addr"
    txtCity_name = "city"
    txtState_name = "state"
    txtPIN_name = "pinno"
    txtPhone_name = "telephoneno"
    txtEmail_name = "emailid"
    txtPass_name = "password"
    btnCustSubmit_name = "sub"

    def __init__(self, driver):
        self.driver = driver

    def click_new_customer_btn(self):
        self.driver.find_element_by_xpath(self.btnAddNewCust_xpath).click()

    def set_cust_name(self, customer):
        self.driver.find_element_by_name(self.txtCustName_name).send_keys(customer)

    def set_gender(self, gender):
        if gender == 'male':
            self.driver.find_element_by_xpath(self.rdMale_xpath).click()
        elif gender == 'female':
            self.driver.find_element_by_xpath(self.rdFemale_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMale_xpath).click()
    time.sleep(5)

    def set_birthdate(self, birthdate):
        self.driver.find_element_by_id(self.txtBirthdate_id).send_keys(birthdate)

    def set_address(self, address):
        self.driver.find_element_by_name(self.txtAddress_name).send_keys(address)

    def set_city(self, city):
        self.driver.find_element_by_name(self.txtCity_name).send_keys(city)

    def set_state(self, state):
        self.driver.find_element_by_name(self.txtState_name).send_keys(state)

    def set_pin(self, pin):
        self.driver.find_element_by_name(self.txtPIN_name).send_keys(pin)

    def set_phone(self, phone):
        self.driver.find_element_by_name(self.txtPhone_name).send_keys(phone)

    def set_email(self, email):
        self.driver.find_element_by_name(self.txtEmail_name).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_name(self.txtPass_name).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_name(self.btnCustSubmit_name).click()
