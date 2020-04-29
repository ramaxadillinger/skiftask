from pages.contact_us import ContactUs
from lib.dom import find_element


def test_submit_form(browser):
    page = ContactUs(browser)()
    page.send_text_to_form()
    page.submit_form()

    assert page.wait_success_submit()
    assert find_element(browser, page.SUCCESS_HEADER).text == "Thank You for your Message!"
