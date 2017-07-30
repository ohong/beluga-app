# Pretty Whale

## Requirement
If not specified, versions are assumed to be recent LTS version.
- A Nvidia graphic card supporting cuDNN i.e. compute capability >= 3.0 (See https://developer.nvidia.com/cuda-gpus)
- Linux: gcc/ g++ 4.8
- Windows: "Microsoft Visual C++ Build Tools 2015" (NOT "Microsoft Visual Studio Community 2015")
- Python 3 (3.5 recommended) ( Python 2.7 needs modifying web host (at least) )
- Numpy
- openCV "cv2" (Python 3 support possible, see installation guide)
- Chainer 2.0.0 or later
- CUDA / cuDNN (If you use GPU)

## Starting web host
UI is html based. using wPaint.js
Server side is very basic python server

boot local server
`python server.py`

access to localhost
`localhost:8000/`


## Learning
main code of colorization is in `cgi-bin/paint_x2_unet`

to train 1st layer using GPU 0 `python train_128.py -g 0`
to train 2nd layer using GPU 0 `python train_x2.py -g 0`

## License
Source code : MIT License

Pre-trained Model : All Rights Reserved

## Acknowledgements
mmm
