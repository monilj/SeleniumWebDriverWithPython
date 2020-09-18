from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class Sliders:
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")


sliders = Sliders()
sliders.test()
