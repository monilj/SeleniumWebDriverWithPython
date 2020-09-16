from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class GetAttribute():
    def getAttributeTest(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")
        print("Value of attribute is: " + result)
        time.sleep(1)
        driver.quit()


getAttribute = GetAttribute()
getAttribute.getAttributeTest()
