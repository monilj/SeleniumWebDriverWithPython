from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

'''
'.'->Class

'''
class FindingAnElementUsingClassWithCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByClassUsingCssSelector = driver.find_element_by_css_selector(".displayed-class")
        if elementByClassUsingCssSelector is not None:
            print("Found an element using Class with CSS Selector")

        listOfElementsByClassUsingCssSelector = driver.find_elements_by_css_selector(".inputs")
        numberOfElementWithClass = len(listOfElementsByClassUsingCssSelector)
        print("Count of elements found with class locator type are " + str(numberOfElementWithClass))

        elementByClassWithTagName = driver.find_element_by_css_selector("input.inputs")
        if elementByClassWithTagName is not None:
            print("Found an element with CSS Selector using Id and TagName")
        driver.quit()


findingAnElementUsingIdWithCSSSelectors = FindingAnElementUsingClassWithCSSSelectors()
findingAnElementUsingIdWithCSSSelectors.test()
