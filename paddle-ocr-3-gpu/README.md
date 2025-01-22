# To start virtual env
```
source paddle-ocr-3-gpu-env/bin/activate
```

monitor gpu use
```
watch -n 1 nvidia-smi > gpu_usage.txt

watch -n 0.1 'echo "$(nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.free --format=csv)\n" >> gpu_usage.txt'


watch -n 0.1 'echo "$(nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.free --format=csv,noheader,nounits)\n" >> gpu_usage.txt'
```

# Installation Instruction
Install paddle gpu

https://www.paddlepaddle.org.cn/documentation/docs/zh/install/pip/linux-pip.html
```
python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/

```

Install paddleOCR
https://paddlepaddle.github.io/PaddleOCR/latest/ppocr/quick_start.html
```
pip install paddleocr
```

paddleocr api
https://paddlepaddle.github.io/PaddleOCR/latest/ppocr/quick_start.html#12-paddleocr-whl

japan_PP-OCRv4