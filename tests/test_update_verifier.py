from src.update_verifier import manifest_is_acceptable


def test_unsigned_manifest_is_rejected():
    assert manifest_is_acceptable({"version": "4.1.0"}) is False


def test_wrong_key_is_rejected():
    manifest = {"signature": "synthetic", "key_id": "UNKNOWN"}
    assert manifest_is_acceptable(manifest) is False