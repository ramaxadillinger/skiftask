from pages.contact_us import ContactUs


def test_submit_form(browser):
    page = ContactUs(browser)()
    page.send_text_to_form()
    page.submit_form()
    assert browser.find_element_by_tag_name('h1').text == "Thank You for your Message!"

    import time; time.sleep(3)
