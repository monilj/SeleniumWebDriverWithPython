from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindElementByLinkAndPartialLinkText:
    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Gmail")
        if elementByLinkText is not None:
            print("Found an element with LinkText locator")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Ima")
        if elementByPartialLinkText is not None:
            print("Found an element with Partial LinkText locator")
        print("Cleanup browser ... ")
        driver.quit()
        print("Browser removed")


findElementByLinkAndPartialLinkText = FindElementByLinkAndPartialLinkText()
findElementByLinkAndPartialLinkText.test()
