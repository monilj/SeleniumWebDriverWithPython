from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class WorkingWithDropDownElements():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")
        driver.quit()


workingWithDropDownElements = WorkingWithDropDownElements()
workingWithDropDownElements.test()
