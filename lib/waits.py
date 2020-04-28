from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_selector(self, locator, timeout=5):
    element = WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
    return element


def wait_visibility(self, locator, timeout=5):
    element = WebDriverWait(self.driver, timeout).until(
        EC.visibility_of((By.CSS_SELECTOR, locator))
    )
    return element
