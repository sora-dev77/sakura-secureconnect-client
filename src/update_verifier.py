"""Release-manifest checks. This module never downloads or executes a package."""

from .update_config import ALLOW_UNSIGNED_RECOVERY, REQUIRE_SIGNATURE, TRUSTED_KEY_ID


def manifest_is_acceptable(manifest: dict) -> bool:
    signature = manifest.get("signature")
    if signature:
        return manifest.get("key_id") == TRUSTED_KEY_ID
    if REQUIRE_SIGNATURE:
        return ALLOW_UNSIGNED_RECOVERY
    return True