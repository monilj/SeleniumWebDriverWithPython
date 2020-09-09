from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindingAnElementUsingIdWithCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByIdUsingCssSelector = driver.find_element_by_css_selector("#displayed-text")
        if elementByIdUsingCssSelector is not None:
            print("Found an element using Id with CSS Selector")
        driver.quit()

findingAnElementUsingIdWithCSSSelectors = FindingAnElementUsingIdWithCSSSelectors()
findingAnElementUsingIdWithCSSSelectors.test()
