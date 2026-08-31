# 🎯 Scoreboard Data Extraction from Video

A Computer Vision project that automatically extracts scoreboard information from a video using image processing and OCR.

---

## 📌 Overview

This project processes a video containing a scoreboard and extracts the relevant scoreboard information.

The system identifies the scoreboard from the video, processes the image, maps the required cells, and extracts the available score data into a structured format.

### Extracted Information

- 👤 Player Names
- 🎳 Rolls
- 📊 Frame Totals
- 🔢 TTL (Total Score)

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **EasyOCR**
- **NumPy**

---

## 📥 Input

The project uses the following input video:

```text
input.mp4


⚙️ Installation

Install the required Python libraries:

pip install opencv-python numpy easyocr

🚀 How to Run

1️⃣ Clone the Repository
git clone <your-repository-url>

2️⃣ Open the Project Folder
cd scoreboard-data-extraction

3️⃣ Install Dependencies
pip install opencv-python numpy easyocr

4️⃣ Run the Project
python main.py

🔄 Project Workflow

The system follows these steps:

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

📤 Output

After processing the video, the project generates the following files:

File	Description
final_scoreboard.json	Extracted scoreboard data in JSON format
final_scoreboard.jpg	Final detected scoreboard image
cell_mapping.jpg	Visualization of mapped scoreboard cells

📊 Output Format

The extracted data is displayed in the terminal in the following format:

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

The extracted scoreboard data is also saved in JSON format.

📁 Project Structure
scoreboard-data-extraction/
│
├── main.py
├── find_coordinates.py
├── input.mp4
│
├── final_scoreboard.json
├── final_scoreboard.jpg
├── cell_mapping.jpg
│
└── README.md

👩‍💻 Author
Sandhya Dhakad







