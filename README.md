# 🎯 Scoreboard Data Extraction from Video

A Computer Vision project that automatically extracts scoreboard information from a video using image processing and OCR.

---

## 📌 Overview

This project processes a video containing a scoreboard and extracts relevant scoreboard information.

The system identifies the scoreboard, processes the image, maps the required cells, and extracts the available score data into a structured format.

### Extracted Information

- 👤 Player Names
- 🎳 Rolls
- 📊 Frame Totals
- 🔢 TTL (Total Score)

---

## 🛠️ Technologies Used

- Python
- OpenCV
- EasyOCR
- NumPy

---

## 📥 Input

The project uses the following input video:

`input.mp4`

> **Note:** The input video is not included in this repository due to its large file size.

---

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install opencv-python numpy easyocr
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Open the Project Folder

```bash
cd scoreboard-data-extraction
```

### 3. Install Dependencies

```bash
pip install opencv-python numpy easyocr
```

### 4. Run the Project

```bash
python main.py
```

---

## 🔄 Project Workflow

```text
Input Video
     ↓
Frame Extraction
     ↓
Scoreboard Detection
     ↓
Scoreboard Cropping
     ↓
Cell Mapping
     ↓
Image Processing
     ↓
OCR Data Extraction
     ↓
Structured Scoreboard Output
```

---

## 📤 Output Files

The project generates the following files:

| File | Description |
|------|-------------|
| `final_scoreboard.json` | Extracted scoreboard data in JSON format |
| `final_scoreboard.jpg` | Final detected scoreboard image |

---

## 📊 Output Format

```text
============================================================
FINAL SCOREBOARD DATA
============================================================

PLAYER: J
Rolls : ['X', '5', '7', '4', ...]
Totals: ['10', '15', '22', '26', ...]
TTL   : 41

============================================================
PROCESSING COMPLETE
============================================================
```

---

## 📁 Project Structure

```text
scoreboard-data-extraction/
│
├── main.py
├── find_coordinates.py
├── mapped_scoreboard.json
├── extracted_scoreboard.json
├── final_scoreboard.json
├── final_scoreboard.jpg
└── README.md
```

---

## 👩‍💻 Author

**Sandhya Dhakad**
