# ANPR-automatic-number-plate-recog-

## Goal: Detect License plate number

## Tools used: OpenCv, Pytorch, Tesseract OCR

## Input Dataset: Images of Cars with License plates

## Steps-

### i) Detection of license plate in image (ML- Haarcascade)
### ii) Cropping out of License plate
### iii) Grey scaling and gaussian blurring of image
### iv) Character segmentation
### v) Character recognition (Multiple ML models tried)
### vi) Model output compared with Tesseract OCR to validate results
### vii) Average performance ~65-70%
