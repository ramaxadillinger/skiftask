from pages.contact_us import ContactUs


def test_reset_form(browser):
    page = ContactUs(browser)()
    page.send_text_to_form()
    page.reset_form()
    d = page.get_values()
    assert d['first_name'] == ''
    assert d['last_name'] == ''
    assert d['email'] == ''
    assert d['message'] == ''

    import time; time.sleep(3)
