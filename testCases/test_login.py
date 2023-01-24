import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    usrername="admin@yourstore.com"
    password="admin"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        get_title=self.driver.title
        self.driver.close()
        if get_title=="Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.usrername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        my_title=self.driver.title
        self.driver.close()
        if my_title =="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False







