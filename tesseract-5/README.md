# Test
See [Tesseract documentation Command Line Usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html#simplest-invocation-to-ocr-an-image) for details
Use --oem 1 for LSTM/neural network, --oem 0 for Legacy Tesseract.
```
tesseract imagename outputbase [-l lang] [--oem ocrenginemode] [--psm pagesegmode] [configfiles...]
```
Fully automatic page segmentation; default is OSD
```
–-psm 3
```

### Simple command
```
tesseract ../test-docs/03_pathological_report.jpg ./res/03_pathological_report_output --oem 1 -l jpn --psm 3
tesseract ../converted-docs/02_pathological_report.jpg ./res/02_pathological_report --oem 1 -l jpn --psm 3 hocr

```

###
Add the following line to the generated hocr script for rendering the UI
```
<script src="https://unpkg.com/hocrjs"></script>
```

### Files
00_breast_examine

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

```
python3 test.py >> result.txt
```