from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class TakeScreenshot:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(6)
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "D::\\selenium_screenshot\\test.png"
        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")
        driver.quit()

takeScreenshot=TakeScreenshot()
takeScreenshot.test()
