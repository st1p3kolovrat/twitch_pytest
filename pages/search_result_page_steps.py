from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_and_open_streamer(self):
        # Waiting for the elements to be present
        wait = WebDriverWait(self.driver, 10)
        all_elements = wait.until(ec.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".Layout-sc-1xcs6mc-0.lkGiNL")))

        # Checking if there are enough elements to scroll to the fourth one
        if len(all_elements) >= 4:
            target_element = all_elements[2]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
            target_element.click()
        else:
            print("Not enough elements to scroll to the fourth one.")