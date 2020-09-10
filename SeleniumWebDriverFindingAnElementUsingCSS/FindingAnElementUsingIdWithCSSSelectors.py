from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

'''
'#'->Id
'''


class FindingAnElementUsingIdWithCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByIdUsingCssSelector = driver.find_element_by_css_selector("#displayed-text")
        if elementByIdUsingCssSelector is not None:
            print("Found an element using Id with CSS Selector")

        elementByIdWithTagName = driver.find_element_by_css_selector("input#name")
        if elementByIdWithTagName is not None:
            print("Found an element with CSS Selector using Id and TagName")
        driver.quit()


findingAnElementUsingIdWithCSSSelectors = FindingAnElementUsingIdWithCSSSelectors()
findingAnElementUsingIdWithCSSSelectors.test()
