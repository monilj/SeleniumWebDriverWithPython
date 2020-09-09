from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindingAnElementUsingMultipleClassWithCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByClassUsingCssSelector = driver.find_element_by_css_selector(".btn-style.class1.class2")
        if elementByClassUsingCssSelector is not None:
            print("Found an element using Multiple Class with CSS Selector")
        driver.quit()


findingAnElementUsingMultipleClassWithCSSSelectors = FindingAnElementUsingMultipleClassWithCSSSelectors()
findingAnElementUsingMultipleClassWithCSSSelectors.test()
