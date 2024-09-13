# AirFirmware - Firmware Download Tool for TB V5.2 Earphones

## Description
AirFirmware is a Python script that facilitates easy downloading and verification of firmware files for TB V5.2 Earphones. The script automates the download process, calculates SHA-256 checksums, and compares them with expected values.

## Features
- Downloading firmware files for various versions
- Automatic calculation of SHA-256 checksums
- Comparing calculated checksums with those of 100% functional firmware files
- Colorful and user-friendly console interface
- Support for multiple firmware versions

## Demo
Check out this video to see how the script works:

![Demo Video](https://github.com/user-attachments/assets/6262df8c-17b3-47c2-ac95-30e92ce677f7)

## Requirements
- Python 3.x
- Libraries:
  - requests
  - tqdm
  - colorama

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Gostrdr1337/AirFirmwareDL.git
   ```
2. Navigate to the project directory:
   ```
   cd AirFirmwareDL
   ```
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```
   python AirFirmwareDownloader.py
   ```
2. Enter the firmware version number you want to download (e.g., 153 (latest) ).
3. The script will download the files and display the checksum verification results.

## Project Structure
- `AirFirmwareDownloader.py`: Main script
- `checksums.json`: File containing expected checksums for different firmware versions
- `README.md`: Description file
- `requirements.txt`: List of required libraries

## Notes
- Ensure you have a stable internet connection when downloading files.
- The script creates separate directories for each downloaded firmware version.

## License
This project is available under the MIT License. See the `LICENSE` file for details.

## Author
Simon - Gostrdr1337

## Contact
For questions or issues, please create a new issue in this repository.
