from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindElementByXpathCSS():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath is not None:
            print("Found an element with XPATH locator")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")
        if elementByCSS is not None:
            print("Found an element with Css locator")
        driver.quit()


findElementByXpathCSS = FindElementByXpathCSS()
findElementByXpathCSS.test()
