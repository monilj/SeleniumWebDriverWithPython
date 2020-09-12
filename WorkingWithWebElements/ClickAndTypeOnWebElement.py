from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class ClickAndTypeOnWebElement():
    def test(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        baseUrl = "https://letskodeit.teachable.com"
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")
        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")
        driver.quit()


clickAndTypeOnWebElement = ClickAndTypeOnWebElement()
clickAndTypeOnWebElement.test()
