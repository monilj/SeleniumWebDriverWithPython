from selenium import webdriver
import time
from UsefulMethodsAndProperties.HandyWrappers import HandyWrappers
from webdriver_manager.firefox import GeckoDriverManager


class UsingWrappersClass():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()


usingWrappersClass = UsingWrappersClass()
usingWrappersClass.test()
