from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindByClassAndTagName():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Check the Element")

        if elementByClassName is not None:
            print("Found an element with  Class Name locator")
        elementByTagName = driver.find_element_by_tag_name("h1")
        textPresent = elementByTagName.text
        if elementByTagName is not None:
            print("Found an element with  Tag Name locator having text " + textPresent)
        driver.quit()


findByClassAndTag = FindByClassAndTagName()
findByClassAndTag.test()
