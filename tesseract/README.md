# Test
See [Tesseract documentation Command Line Usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html#simplest-invocation-to-ocr-an-image) for details
Use --oem 1 for LSTM/neural network, --oem 0 for Legacy Tesseract.
```
tesseract imagename outputbase [-l lang] [--oem ocrenginemode] [--psm pagesegmode] [configfiles...]
```

### Simple command
```
tesseract 01_breast_x-ray_report.jpg output --oem 1 -l jpn
tesseract ../test-docs/01_breast_x-ray_report.jpg ./res/01_breast_x-ray_report_output.txt --oem 1 -l jpn
tesseract ../test-docs/01_breast_x-ray_report.jpg ./res/01_breast_x-ray_report_output.txt --oem 1 -l jpn hocr
```
### Output
# 00
```
Tesseract Open Source OCR Engine v4.1.1 with Leptonica
Detected 154 diacritics
```
# 01
```
Tesseract Open Source OCR Engine v4.1.1 with Leptonica
Warning: Invalid resolution 0 dpi. Using 70 instead.
Estimating resolution as 174
```
# 02
```
Tesseract Open Source OCR Engine v4.1.1 with Leptonica
Detected 69 diacritics
```
# 03
```
Tesseract Open Source OCR Engine v4.1.1 with Leptonica
Detected 131 diacritics
```

