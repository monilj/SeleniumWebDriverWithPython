from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class ElementState():
    def isEnabled(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        element1 = driver.find_element_by_id("gs_htif0")
        element1State = element1.is_enabled()  # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(element1State))

        element2 = driver.find_element_by_id("gs_taif0")
        element2State = element2.is_enabled()  # True for enabled and False for disabled
        print("E2 is Enabled? -> " + str(element2State))

        element3 = driver.find_element_by_id("lst-ib")
        element3State = element3.is_enabled()  # True for enabled and False for disabled
        print("E3 is Enabled? -> " + str(element3State))

        element3.send_keys("letskodeit")


elementState = ElementState()
elementState.isEnabled()
