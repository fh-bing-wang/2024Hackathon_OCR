# Official Site
https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md

Run image in docker
Just using CPU
```
sudo docker run --name ppocr -v $PWD:/paddle --network=host -it registry.baidubce.com/paddlepaddle/paddle:2.1.3-gpu-cuda10.2-cudnn7  /bin/bash
```

```
# ctrl+P+Q to exit docker, to re-enter docker using the following command:
sudo docker container exec -it ppocr /bin/bash
```

Copy file to docker container
```
docker cp test-docs/01_breast_x-ray_report.jpg e61403a346cf:/home/test_docs
docker cp e61403a346cf:/home/paddle_ocr/res res
```

Install Install PaddleOCR Whl Package
```
python3 -m pip install paddlepaddle
pip3 install "paddleocr>=2.6.0.3"
```

Run OCR in the command line
```
paddleocr --image_dir ./test_docs/01_breast_x-ray_report.jpg --lang=japan
```


Should use GPU; check sudo docker run --name ppocr -v $PWD:/paddle --network=host -it  registry.baidubce.com/paddlepaddle/paddle:2.1.3-gpu-cuda10.2-cudnn7  /bin/bash
```
# If using GPU, use nvidia-docker to create docker
# docker image registry.baidubce.com/paddlepaddle/paddle:2.1.3-gpu-cuda11.2-cudnn8 is recommended for CUDA11.2 + CUDNN8.
sudo nvidia-docker run --name ppocr -v $PWD:/paddle --shm-size=30G --network=host -it registry.baidubce.com/paddlepaddle/paddle:2.1.3-gpu-cuda10.2-cudnn7 /bin/bash
```

# Installed package verions
paddleocr                         2.7.0.2
paddlepaddle                      2.5.2

Name: paddlepaddle
Version: 2.5.2
Summary: Parallel Distributed Deep Learning
Home-page: https://www.paddlepaddle.org.cn/
Author: 
Author-email: Paddle-better@baidu.com
License: Apache Software License
Location: /usr/local/python3.7.0/lib/python3.7/site-packages
Requires: decorator, protobuf, numpy, Pillow, astor, opt-einsum, httpx
Required-by: 


Name: paddleocr
Version: 2.7.0.2
Summary: Awesome OCR toolkits based on PaddlePaddle （8.6M ultra-lightweight pre-trained model, support training and deployment among server, mobile, embeded and IoT devices
Home-page: https://github.com/PaddlePaddle/PaddleOCR
Author: 
Author-email: 
License: Apache License 2.0
Location: /usr/local/python3.7.0/lib/python3.7/site-packages
Requires: Pillow, fonttools, numpy, premailer, attrdict, PyMuPDF, visualdl, scikit-image, beautifulsoup4, python-docx, lmdb, imgaug, pdf2docx, lxml, opencv-contrib-python, openpyxl, rapidfuzz, shapely, cython, pyclipper, tqdm, opencv-python, fire
Required-by: