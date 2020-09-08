from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FindByIdName:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("Found an element with ID locator")

        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("Found an element with NAME locator")
        driver.quit()


findByIdName = FindByIdName()
findByIdName.test()
