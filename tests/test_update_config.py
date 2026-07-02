from src import update_config


def test_stable_channel_requires_signatures():
    assert update_config.CHANNEL == "stable"
    assert update_config.REQUIRE_SIGNATURE is True
    assert update_config.ALLOW_UNSIGNED_RECOVERY is False