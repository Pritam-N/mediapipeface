# mediapipeface

This is a package using mediapipe for face detection and mesh creation. 

It has two modules:
    
    1. facedetectmodule for face detection from video/webcam
    2. facemeshmodule for generating module from video/webcam

Works well using mp4 videos. 

## installation

Run the following to install:
```python
pip install mediapipeface
```

## usage

```python
import facedetectmodule as fdm
fdm.main('sample.mp4')
```

## develop
```bash
$ pip install -e .[dev]
```