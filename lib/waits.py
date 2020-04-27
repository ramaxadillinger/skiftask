from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_selector(self, locator, timeout):
    element = WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
    return element
