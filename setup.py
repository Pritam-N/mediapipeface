from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='mediapipeface',
    version='0.1.0',
    description='Mediapipe face implementations.',
    url='https://github.com/Pritam-N/mediapipeface',
    author='Pritama Nayak',
    author_email='nayak264@gmail.com',
    py_modules=['helloworld', 'facedetectmodule','facemeshmodule'],
    package_dir={'':'src'},

    long_description = long_description,
    long_description_content_type = 'text/markdown',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'

    ],
    install_requires = [
        'mediapipe >= 0.8',
        'opencv-python',
    ],
    extras_require = {
        'dev': [
            'pytest>=3.7'
        ]
    }
)