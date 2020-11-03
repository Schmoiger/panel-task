import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.etup(
    name='panel-test-pkg',
    version='0.1',
    description='Module for panel interview',
    url='https://www.learnopencv.com/faster-r-cnn-object-detection-with-pytorch'
    packages=setuptools.find_packages(),
    install_requires=[requirements],  # external packages as dependencies
    python_requires='>=3.6'
)
