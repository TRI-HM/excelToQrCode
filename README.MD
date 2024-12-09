"""
This script converts an Excel file to QR codes for each row in the file.

Usage:
1. Install the required packages in a new environment:
  ```
  pip install pandas openpyxl qrcode[pil]
  ```
2. Place your Excel file in the same directory as this script.
3. Run the script:
  ```
  python index.py <path_to_excel_file>
  ```
4. The script will generate QR codes for each row in the Excel file and save them as images in the output directory.

Parameters:
- <path_to_excel_file>: The path to the Excel file you want to convert to QR codes.
