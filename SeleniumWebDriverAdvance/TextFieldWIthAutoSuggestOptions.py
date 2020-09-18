from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class OptionSelectionFromAutoSuggest:
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.XPATH, "//span[text()='Flights']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").send_keys("SFO")
        driver.find_element(By.XPATH, "// strong[contains(text(), 'SFO')]").click()
        driver.quit()


optionSelectionFromAutoSuggest = OptionSelectionFromAutoSuggest()
optionSelectionFromAutoSuggest.test()

