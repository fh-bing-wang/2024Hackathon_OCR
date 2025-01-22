# To start virtual env
```
source paddle-ocr-3-env/bin/activate
```

monitor gpu use
```
watch -n 1 nvidia-smi > gpu_usage.txt

watch -n 1 'echo "$(nvidia-smi --query-gpu=name,utilization.gpu,memory.total,memory.used,memory.free --format=csv,noheader)\n" >> gpu_usage.txt'


watch -n 1 'echo "$(nvidia-smi --query-compute-apps=pid,process_name,used_gpu_memory,memory_usage --format=csv,noheader)" >> gpu_usage_1000.txt'
```

# Installation
Install paddle gpu
https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/develop/install/pip/linux-pip.html
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