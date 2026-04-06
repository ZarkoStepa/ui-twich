def test_twitch_flow(driver):
    from pages.twitch_page import TwitchPage

    twitch = TwitchPage(driver)

    twitch.open_twitch()
    twitch.click_browse()
    twitch.search("StarCraft II")
    twitch.scroll()
    twitch.click_first_streamer()
    twitch.verify_stream_loaded()