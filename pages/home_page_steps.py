import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def close_modal(self):
        wait = WebDriverWait(self.driver, 3)
        try:
            # Attempt to close the modal
            close_modal_button = wait.until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, "[data-a-target='tw-core-button-label-text']")))
            close_modal_button.click()
        except Exception as e:
            print("Modal did not appear or could not be closed:", str(e))

    def click_search_btn(self):
        # Click search button
        wait = WebDriverWait(self.driver, 3)
        search_button = wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/search'][aria-label='Search']")))
        search_button.click()

    def enter_search_term(self, search_term):
        wait = WebDriverWait(self.driver, 3)
        search_field = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']")))
        search_field.send_keys(search_term)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)
