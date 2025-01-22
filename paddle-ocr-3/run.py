from paddleocr import PaddleOCR, draw_ocr
import os
from PIL import Image
import time

duration = 0
count = 0

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="japan")  # need to run only once to download and load model into memory

folder_path = '../test-docs-1000'
res_path = './res_converted/'

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        img_path = file_path

        start_time = time.time()
        result = ocr.ocr(img_path, cls=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        duration += elapsed_time
        count += 1
        
        print(f"Processed {file_path} duration: {duration:.2f} {count}/1000")
        
        # with open(f"{res_path}{file_name}_text.txt", 'w') as file:
        #     for idx in range(len(result)):
        #         res = result[idx]
        #         for line in res:
        #             print(line[1][0] + '\n')
        #             file.write(line[1][0] + '\n')
        # print(f"created {file_name}_text.txt")

        # # 显示结果
        # result = result[0]
        # image = Image.open(img_path).convert('RGB')
        # boxes = [line[0] for line in result]
        # txts = [line[1][0] for line in result]
        # scores = [line[1][1] for line in result]
        # im_show = draw_ocr(image, boxes, txts, scores, font_path='./PretendardJP-Regular.ttf')
        # im_show = Image.fromarray(im_show)
        # im_show.save(f"{res_path}{file_name}_img.jpg")

        # print(f"created {file_name}_img.txt")