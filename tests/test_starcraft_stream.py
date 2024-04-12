def test_starcraft_stream(driver, home_page, common_steps, search_result_page):
    home_page.close_modal()
    home_page.click_search_btn()
    home_page.enter_search_term("StarCraft II")
    search_result_page.scroll_and_open_streamer()
    common_steps.take_screenshot()
