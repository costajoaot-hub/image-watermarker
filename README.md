# Photo Branding & Watermark Automator

A Python utility designed to prepare photography contest winners for web publication. This tool automatically appends a professional black branding bar to the bottom of images, featuring the author's name cross-referenced from an Excel database.

## Features

* **Dynamic Footer Generation:** Adds a consistent black bar at the bottom of images without cropping the original content.
* **Excel Data Integration:** Automatically matches image filenames (e.g., `288.jpg`) with metadata (e.g., Author Name) stored in an `.xlsx` file.
* **Auto-Scaling Typography:** Adjusts text placement and sizing to remain centered and legible regardless of image dimensions.
* **Batch Processing:** Handles multiple file formats (PNG, JPG, JPEG) in one execution, maintaining high-quality output (95% JPEG quality).

## Requirements

* **Python 3.x**
* **Pillow (PIL):** For advanced image manipulation.
* **Pandas & Openpyxl:** For spreadsheet data handling.

Install the dependencies via pip:
```bash
pip install Pillow pandas openpyxl

python main.py
