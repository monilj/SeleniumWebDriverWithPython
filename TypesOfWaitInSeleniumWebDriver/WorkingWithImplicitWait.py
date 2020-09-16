from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class WorkingWithImplicitWait:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")
        driver.quit()


workingWithImplicitWait = WorkingWithImplicitWait()
workingWithImplicitWait.test()
