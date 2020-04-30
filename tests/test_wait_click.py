from pages.loader import Loader


def test_wait_click(browser):
    page = Loader(browser)()
    page.wait_button_click_me()
    page.click_me()
    assert page.wait_modal()
    page.click_close()


def test_modal_close(browser):
    page = Loader(browser)()
    page.wait_button_click_me()
    page.click_me()
    page.wait_modal()
    page.click_close()
    assert page.button_click_me_is_present()
