from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class RunFirstChromeTest:
    def openUrlInChrome(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://techlistic.com/")


chrome_instance = RunFirstChromeTest()
chrome_instance.openUrlInChrome()
