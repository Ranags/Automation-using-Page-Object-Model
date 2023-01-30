from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MacrhantLogin:
    textbox_email_xpath = "//div[@class='c-PJLV c-PJLV-ifgNTsQ-css']//div[@class='c-haPTvi c-haPTvi-bujJeW-size-md']"
    textbox_password_xpath = "//div[@class='c-PJLV c-PJLV-iJbCqM-css']//div[@class='c-haPTvi c-haPTvi-bujJeW-size-md']"
    button_login_xpath = "//button[@class='c-leIVPW c-leIVPW-lbzlto-size-lg c-leIVPW-MnczI-color-red c-leIVPW-ikJzvVT-css']"



    def __init__(self,driver):
        self.driver=driver


    def setUserName(self,username):
        time.sleep(2)
        self.driver.find_element(By.ID, self.textbox_email_xpat).clear()
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_email_xpath).send_keys(username)



    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_xpath).clear()
        self.driver.find_element(By.ID, self.textbox_password_xpath).send_keys(password)



    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()















