from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class JavaScriptExecution:
    def test(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)
        time.sleep(6)
        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


javaScriptExecution = JavaScriptExecution()
javaScriptExecution.test()
