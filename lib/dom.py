from selenium.webdriver.common.by import By


def find_element(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator)


def send_keys(driver, input_loc, text):
    element = find_element(driver, input_loc)
    return element.send_keys(text)


def click_button(driver, btn_loc):
    return find_element(driver, btn_loc).click()


def get_text(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator).get_attribute("value")
