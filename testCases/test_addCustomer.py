import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import addCustomer
from selenium.webdriver.common.by import By
class Test_003_AddCustomer:
    baseURL = "https://admin-demo.nopcommerce.com/"
    usrername = "admin@yourstore.com"
    password = "admin"

    def test_addCustomer(self, setup):
        # self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usrername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.logger.info("************* Login succesful **********")


        # self.logger.info("************* Login succesful **********")

        self.addcust = addCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        # self.logger.info("************* Providing customer info **********")


        self.addcust.setEmail("goharrana6@gmail.com")
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        # self.logger.info("************* Saving customer info **********")
        #
        # self.logger.info("********* Add customer validation started *****************")

        # self.msg = self.driver.find_element(By.LINK_TEXT,"body").text
        #
        # print(self.msg)
        # if 'customer has been added successfully.' in self.msg:
        #     assert True
        #     self.logger.info("********* Add customer Test Passed *********")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
        #     self.logger.error("********* Add customer Test Failed ************")
        #     assert False
        #
        # self.driver.close()










