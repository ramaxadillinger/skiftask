from pages.loader import Loader


def test_waiting_present_of_button_click_me(browser):
    loader = Loader(browser)()
    loader.wait_button_click_me()
    loader.click_me()
    assert loader.wait_modal()
    loader.click_close()


def test_if_button_click_me_is_visible(browser):
    loader = Loader(browser)()
    loader.wait_button_click_me()
    loader.click_me()
    loader.wait_modal()
    loader.click_close()
    assert loader.button_click_me_is_present()
