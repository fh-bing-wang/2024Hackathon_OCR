from PIL import Image, ImageOps, ImageFilter
import pytesseract
import time
import os

repo_path = '../test-docs-5000'
duration = 0
count = 0

# Loop through every file in the directory
for root, dirs, files in os.walk(repo_path):
    for file in files:
        file_path = os.path.join(root, file)
        config = '--oem 1 -l jpn --psm 3'
        
        image = Image.open(file_path)
        
        start_time = time.time()
        
        # Extract text from the preprocessed image.
        improved_text = pytesseract.image_to_string(image, config=config)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        duration += elapsed_time
        count += 1
        # Print the extracted text.
        print(f"Processed {len(improved_text)} words {file_path} duration: {duration:.2f} seconds {count}/5000")

print(f"Time taken to process: {duration:.2f} seconds\n")
# # Convert image to grayscale.
# gray_image = ImageOps.grayscale(image)

# # Resize the image to enhance details.
# scale_factor = 2
# resized_image = gray_image.resize(
#     (gray_image.width * scale_factor, gray_image.height * scale_factor),
#     resample=Image.LANCZOS
# )

# # Apply adaptive thresholding using the `FIND_EDGES` filter.
# thresholded_image = resized_image.filter(ImageFilter.FIND_EDGES)

