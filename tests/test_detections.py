import tests.detect_images as detect_images
import json
import pytest


@pytest.fixture
def images_detected(scope="session"):
    images = detect_images.parse_images()
    result_json = detect_images.detect_images(images)
    return images, result_json


def test_valid_json(images_detected):
    images, result_json = images_detected
    error = False
    try:
        r = json.loads(result_json)
        error = False
    except:
        error = True
    assert error == False


def test_confirm_all_processed(images_detected):
    images, result_json = images_detected
    error = False
    if len(images) == len(json.loads(result_json)):
        error = False
    else:
        error = True
    assert error == False


def test_at_least_one_result(images_detected):
    images, result_json = images_detected
    error = False
    for result in json.loads(result_json):
        if result['detections'] == []:
            error = True
        else:
            error = error or False
    assert error == False
