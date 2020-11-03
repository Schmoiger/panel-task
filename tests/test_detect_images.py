from src.object_detection import object_detection_api
import pytest


'''
def test_add():
    result = add(12, 4)
    assert result == 16
'''

object_detection_api('./tests/dog.jpg', threshold=0.8)
