from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class WorkingWithWindowSize:
    def test(self):
        option = Options()
        option.add_argument("window-size=1400,600")
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        # Get window Size
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))

        # Get window size using direct method

        driver.get_window_size()
        driver.set_window_size(1920, 1080)


workingWithWindowSize = WorkingWithWindowSize()
workingWithWindowSize.test()
