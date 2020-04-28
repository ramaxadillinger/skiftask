from lib.dom import send_keys
from lib.dom import click_button, get_text
from lib.urls import URL
from lib.waits import wait_selector, wait_visibility


DATA = {
    'first_name': 'Ivan',
    'last_name': 'Moldovan',
    'email': 'moldova@gmail.com',
    'message': 'fuck you'
}


class ContactUs(object):
    FIRST_NAME = '[name="first_name"]'
    LAST_NAME = '[name="last_name"]'
    EMAIL = '[name="email"]'
    MESSAGE = '[name="message"]'
    BUTTON_SUBMIT = '[type="submit"]'
    BUTTON_RESET = '[type="reset"]'

    SUCCESS_HEADER = 'h1'

    def __init__(self, driver):
        self.driver = driver

    def __call__(self):
        self.driver.get(URL)
        wait_selector(self, self.FIRST_NAME, 10)
        return self

    def send_text_to_form(self):
        send_keys(self.driver, self.FIRST_NAME, DATA['first_name'])
        send_keys(self.driver, self.LAST_NAME, DATA['last_name'])
        send_keys(self.driver, self.EMAIL, DATA['email'])
        send_keys(self.driver, self.MESSAGE, DATA['message'])

    def wait_success_submit(self):
        return wait_visibility(self.driver, self.SUCCESS_HEADER)

    def submit_form(self):
        click_button(self.driver, self.BUTTON_SUBMIT)

    def get_values(self):
        d = {}
        d['first_name'] = get_text(self.driver, self.FIRST_NAME)
        d['last_name'] = get_text(self.driver, self.LAST_NAME)
        d['email'] = get_text(self.driver, self.EMAIL)
        d['message'] = get_text(self.driver, self.EMAIL)
        return d

    def check_empty_fields(self):
        d = self.get_values()
        assert d['first_name'] == ''
        assert d['last_name'] == ''
        assert d['email'] == ''
        assert d['message'] == ''

    def reset_form(self):
        click_button(self.driver, self.BUTTON_RESET)








