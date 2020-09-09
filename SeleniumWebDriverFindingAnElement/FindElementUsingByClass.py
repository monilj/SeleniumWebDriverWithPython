from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class FindElementUsingBy():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("Found an element by Id locator")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("Found an element by XPATH locator")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("Found an element by Link Text locator")
        driver.quit()


findElementUsingBy = FindElementUsingBy()
findElementUsingBy.test()
