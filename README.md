# Blood Vessel Segmentation in Retinal Images

A classical image-processing pipeline that automatically segments blood vessels from retinal fundus images — no deep learning required. Early signs of conditions like **diabetic retinopathy** and **glaucoma** often appear in retinal vessel patterns before symptoms show, and manual detection is tedious and examiner-dependent. This project automates that detection using traditional computer vision techniques.

## 🧪 Pipeline

```
Input Retinal Image (RGB)
        ↓
Green Channel Extraction
        ↓
CLAHE Enhancement
        ↓
Black-Hat Transform
        ↓
Binary Thresholding
        ↓
Morphological Opening
        ↓
Output: Segmented Vessel Mask
```

### Steps Explained

1. **Green Channel Extraction** — Blood vessels appear darkest in the green channel of an RGB fundus image, giving the highest contrast among the three color channels.
2. **CLAHE (Contrast Limited Adaptive Histogram Equalization)** — Enhances local contrast in tiles to make thin, faint vessels more visible without over-amplifying noise.
3. **Black-Hat Morphological Transform** — Reveals dark vessel structures against the bright retinal background using a 15×15 elliptical structuring element.
4. **Binary Thresholding (Otsu's method)** — Automatically determines the optimal threshold to separate vessel pixels from background, producing a binary mask.
5. **Morphological Opening** — Removes small noise spots (erosion + dilation with a 3×3 elliptical kernel) to produce a clean final vessel mask.

## 🛠️ Tech Stack

- **OpenCV** (`cv2`) — image processing operations
- **NumPy** — array operations

## 📁 Files

| File | Description |
|------|-------------|
| `retina.py` | Full segmentation pipeline script |
| `Jemima_James_image_processing_report.pdf` | Project report — objectives, assumptions, system architecture, results |

##  Usage

```bash
python retina.py
```

Update the image path in `segment_vessels()` to point to your retinal fundus image. The script displays each pipeline stage (Original → Green Channel → CLAHE → Black-Hat → Threshold → Final Mask) in separate resizable windows.

##  Assumptions & Limitations

- Input must be a standard RGB retinal fundus photograph with a circular field of view and dark background
- Image needs sufficient brightness/resolution for CLAHE to work effectively
- Valid only for healthy or mildly affected retinas — severe lesions or haemorrhages may cause false detections
- Grayscale images are not supported (green channel extraction requires 3-channel RGB input)

##  Objectives

- Extract the green channel to maximize vessel-to-background contrast
- Enhance faint/thin vessel visibility via CLAHE
- Isolate dark vessel structures using Black-Hat transform
- Automatically binarize using Otsu thresholding
- Remove noise via morphological opening
- Visually verify each pipeline stage

---
*Image Processing Project — Classical Computer Vision (No Deep Learning)*
