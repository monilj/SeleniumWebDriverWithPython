from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class UseOfWildCardClassWithCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByWildCardStartWith = driver.find_elements_by_css_selector("input[class^='input']")
        numberOfElement = len(elementByWildCardStartWith)
        if elementByWildCardStartWith is not None:
            print("Number of elements found using wild card Start with in CSS Selector" + str(numberOfElement))

        elementByWildCardEndsWith = driver.find_element_by_css_selector("input[class$='displayed-class']")
        if elementByWildCardEndsWith is not None:
            print("Found using wild card Ends with in CSS Selector")

        elementByWildCardContains = driver.find_element_by_css_selector("input[placeholder*='Example']")
        if elementByWildCardContains is not None:
            print("Found using wild card Contains with in CSS Selector")
        driver.quit()


useOfWildCardClassWithCSSSelectors = UseOfWildCardClassWithCSSSelectors()
useOfWildCardClassWithCSSSelectors.test()
