from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def wait_selector(driver, locator, timeout=5):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
    return element


def wait_visibility(driver, locator, timeout=5):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of(
            driver.find_element(By.CSS_SELECTOR, locator)
        )
    )
    return element


def wait_click_element(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
    )
    return element


def is_disappeared(driver, locator, timeout=5):
    element = WebDriverWait(driver, timeout).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
    return element
