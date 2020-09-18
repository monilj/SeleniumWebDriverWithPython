from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class MouseHoverAction:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")


mouseHoverAction = MouseHoverAction()
mouseHoverAction.test()
