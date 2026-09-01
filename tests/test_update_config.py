from src import update_config


def test_stable_channel_configuration():
    assert update_config.CHANNEL == "stable"
    assert update_config.UPDATE_CHANNEL_URL.startswith("https://")