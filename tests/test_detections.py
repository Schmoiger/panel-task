import tests.detect_images as detect_images
import json


def test_prerequisites():
    try:
        images = detect_images.parse_images()
        result_json = detect_images.detect_images(images)
        prereq_complete = True
    except:
        prereq_complete = False
    assert prereq_complete == True


def test_valid_json():
    try:
        r = json.loads(result_json)
        error = False
    except:
        error = True
    assert error == False


def test_confirm_all_processed():
    if len(images) == len(json.loads(result_json)):
        error = False
    else:
        error = True
    assert error == False


def test_at_least_one_result():
    error = False
    for key, value in json.loads(result_json):
        if value == '':
            error = True
        else:
            error = error or False
    assert error == False
