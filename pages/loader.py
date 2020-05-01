from lib.dom import click_button
from lib.urls import LOADER_URL
from lib.waits import wait_click_element, wait_visibility, wait_disappeared


class Loader(object):
    BUTTON_CLICK_ME = '[id="button1"]'
    MODAL_CLICK = '[id="myModalClick"]'
    BUTTON_CLOSE = '[class="btn btn-default"]'

    def __init__(self, driver):
        self.driver = driver

    def __call__(self):
        self.driver.get(LOADER_URL)
        return self

    def wait_button_click_me(self):
        return wait_click_element(self.driver, self.BUTTON_CLICK_ME)

    def click_me(self):
        click_button(self.driver, self.BUTTON_CLICK_ME)

    def wait_modal(self):
        return wait_visibility(self.driver, self.MODAL_CLICK)

    def click_close(self):
        click_button(self.driver, self.BUTTON_CLOSE)

    def button_click_me_is_present(self):
        return wait_visibility(self.driver, self.BUTTON_CLICK_ME)
