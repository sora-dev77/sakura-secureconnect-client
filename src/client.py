"""Minimal SecureConnect client metadata used by the training repository."""

PRODUCT_NAME = "Sakura SecureConnect VPN"
CLIENT_VERSION = "4.2.0"


def client_banner() -> str:
    return f"{PRODUCT_NAME} {CLIENT_VERSION}"