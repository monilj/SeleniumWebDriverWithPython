from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class RunFirstFFTest:
    def openUrlOnFireFox(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("http://techlistic.com/")


ff_instance = RunFirstFFTest()
ff_instance.openUrlOnFireFox()
