import tests.detect_images as detect_images
import json
import pytest


@pytest.fixture
def images_detected(scope="session"):
    images = parse_images()
    result_json = detect_images(images)


def test_valid_json(images_detected):
    try:
        r = json.loads(result_json)
        error = False
    except:
        error = True
    assert error == False


def test_confirm_all_processed(images_detected):
    if len(images) == len(json.loads(result_json)):
        error = False
    else:
        error = True
    assert error == False


def test_at_least_one_result(images_detected):
    error = False
    for key, value in json.loads(result_json):
        if value == '':
            error = True
        else:
            error = error or False
    assert error == False
