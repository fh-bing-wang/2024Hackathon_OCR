import easyocr
import os
import time

reader = easyocr.Reader(['ja', 'en'], gpu = True)
#reader = easyocr.Reader(['ja', 'en'], gpu = False)
folder_path = '../test-docs-1000'
duration = 0
count = 0

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        img_path = file_path
        
        start_time = time.time()
        result = reader.readtext(img_path, detail = 0, paragraph=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        duration += elapsed_time
        count += 1
        
        # with open(f"./res_converted/{file_name}_text.txt", 'w') as file:
        #     for line in result:
        #         file.write(line + '\n')
        print(f"Processed {file_name}_text.txt duration: {duration:.2f} {count}/5000")

print(f"Time taken to process: {duration:.2f} seconds\n")
