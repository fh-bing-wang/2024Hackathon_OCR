## Installed CUDA
https://developer.nvidia.com/cuda-12-3-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_network
Cuda-driver does not work

sudo apt-get install -y cuda-drivers
works, but refer to a different version


## Batch create test files
```
mkdir -p test-docs-50 && for file in test-docs/*; do for i in $(seq 1 50); do cp "$file" "test-docs-50/$(basename "${file%.*}")_copy${i}.${file##*.}"; done; done

mkdir -p test-docs-1000 && for file in test-docs/*; do for i in $(seq 1 1000); do cp "$file" "test-docs-1000/$(basename "${file%.*}")_copy${i}.${file##*.}"; done; done
```

## Write to output GPU memory use
```
watch -n 1 'echo "$(nvidia-smi --query-gpu=name,utilization.gpu,memory.used,memory.free --format=csv,noheader,nounits)" >> gpu_usage_1000.txt'
 

watch -n 1 'echo "$(nvidia-smi --query-compute-apps=pid,process_name,used_gpu_memory --format=csv,noheader)" >> gpu_usage_1000_2.txt'

nvidia-smi --query-compute-apps=pid,process_name,used_gpu_memory --format=csv
```

## Monitor CPU memory use
```
COLUMNS=1000 top -b -d 1 -c | grep paddle >> paddle_cpu_usage.txt
```



nvidia-smi 
Tue Dec  3 12:20:24 2024       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.42.06              Driver Version: 555.42.06      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Tesla V100-SXM2-16GB           Off |   00000000:00:1E.0 Off |                    0 |
| N/A   31C    P0             25W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
