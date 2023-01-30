
from pageObjects.MarchantLogin import MacrhantLogin

class Test_01_MarchantLogin:
    baseURL = ""
    usrername = ""
    password = ""


    def test_MarchantLogin(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp = MacrhantLogin(self.driver)
        self.lp.setUserName(self.usrername)
        self.lp.setPassword(self.password)





