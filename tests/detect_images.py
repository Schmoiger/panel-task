import src.object_detection as object_detection
import wget
import json

TEST_FOLDER = './tests/'
IMAGE_FILE = 'images.txt'
DETECTION_THRESHOLD = 0.8


def parse_images(test_images=TEST_FOLDER+IMAGE_FILE):
    # parse images list
    try:
        with open(test_images) as file:
            lines = [line.rstrip() for line in file]
        images = [line for line in lines if (line != '' and not(line.startswith('#')))]
    except:
        error_status = 'invalid image file'
        return error_status

    # download into tests folder if not already downloaded; append full file path
    for i in range(len(images)):
        filename = images[i].rsplit('/', 1)[-1]
        if images[i].startswith('http'):
            print(filename)
            try:
                wget.download(images[i], TEST_FOLDER + filename)
                images[i] = TEST_FOLDER + filename
            except:
                pass
        else:
            images[i] = TEST_FOLDER + filename

    # if not downloadable, remove from list
    downloaded_images = [image for image in images if not(image.startswith('http'))]
    return downloaded_images


def detect_images(images):
    # run object detection on each image
    detections = []
    for image in images:
        _, labels = object_detection.get_prediction(image, DETECTION_THRESHOLD)
        detections.append({
            'image_filename': image,
            'detections': labels
        })

    detections_json = json.dumps(detections)
    return detections_json
