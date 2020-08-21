from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager


class RunFirstIETest:
    def openUrlOnIE(self):
        driver = webdriver.Ie(IEDriverManager().install())
        driver.get("http://letskodeit.com")


ie_instance = RunFirstIETest()
ie_instance.openUrlOnIE()
