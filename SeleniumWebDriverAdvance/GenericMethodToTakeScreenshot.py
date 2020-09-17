from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class ScreenShotUsingGenericMethod:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self, driver):
        """Takes screenshot of the current open web page
            :param driver
            :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "D:\\selenium_screenshot\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


screenShotUsingGenericMethod = ScreenShotUsingGenericMethod()
screenShotUsingGenericMethod.test()
