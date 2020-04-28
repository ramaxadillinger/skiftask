from pages.contact_us import ContactUs


def test_reset_form(browser):
    page = ContactUs(browser)()
    page.send_text_to_form()
    page.reset_form()

    page.check_empty_fields()
