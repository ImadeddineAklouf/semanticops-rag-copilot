from app.core.logging import configure_logging


def test_logging_configuration():
    configure_logging()

    assert True