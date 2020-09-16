from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WorkingWithExplicitWait:
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.XPATH, "//span[text()='Flights']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']").send_keys("SFO")
        driver.find_element(By.XPATH, "// strong[contains(text(), 'SFO')]").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Going to']").send_keys("NYC")
        driver.find_element(By.XPATH, "//strong[contains(text(), 'LGA')]").click()
        driver.find_element(By.ID, "d1-btn").click()
        driver.find_element(By.XPATH, "//div[@class='uitk-new-date-picker-month'][1]//button[@data-day='30']").click()
        driver.find_element(By.XPATH, "//div[@class='uitk-new-date-picker-month'][2]//button[@data-day='1']").click()
        driver.find_element(By.XPATH, "//span[text()='Done']").click()
        driver.find_element(By.XPATH, "//button[@data-testid='submit-button']").click()
        wait = WebDriverWait(driver, 20, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='fch0']")))
        element.click()
        time.sleep(2)
        driver.quit()


workingWithExplicitWait = WorkingWithExplicitWait()
workingWithExplicitWait.test()
