from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindingAnElementUsingChildNodeCSSSelectors():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementUsingChildNodeInCSS = driver.find_element_by_css_selector("fieldset>table")
        if elementUsingChildNodeInCSS is not None:
            print("Found an element using Child node in CSS Selector")

        driver.quit()


findingAnElementUsingChildNodeCSSSelectors = FindingAnElementUsingChildNodeCSSSelectors()
findingAnElementUsingChildNodeCSSSelectors.test()
