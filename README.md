# AirFirmware - Firmware Download Tool for Earphones

## Description
AirFirmware is a Python script that facilitates easy downloading and verification of firmware files for Earphones. The script automates the download process, calculates SHA-256 checksums, and compares them with expected values to ensure the integrity of the firmware.

## Features
- Downloading firmware files for various versions
- Automatic calculation of SHA-256 checksums
- Comparing calculated checksums with those of 100% functional firmware files
- Colorful and user-friendly console interface
- Support for multiple firmware versions
- Includes a `Firmware-backup` folder with pre-downloaded firmware bin files
- Each firmware version in the `Firmware-backup` folder is accompanied by a checksum file for safety and integrity verification.

## Demo
Check out this video to see how the script works:

![Demo Video](https://github.com/user-attachments/assets/406b75e9-5357-4104-9691-794eccb56691)

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
2. Enter the firmware version number you want to download (e.g., `153` for the latest version).
3. The script will download the files and display the checksum verification results.

### Firmware-Backup Folder
- In addition to the automated download feature, this repository includes a `Firmware-backup` folder that contains pre-downloaded `.bin` firmware files.
- Each firmware file is accompanied by a corresponding checksum file (`checksums.txt`) that contains the expected SHA-256 hash for the firmware.
- To ensure the firmware file’s integrity, you can verify the downloaded firmware’s checksum by using an online SHA-256 checker or any other checksum tool you prefer.

**To verify the checksum:**
1. Open an online SHA-256 checksum tool such as [this one](https://emn178.github.io/online-tools/sha256_checksum.html), or use another checksum tool of your choice (e.g., `shasum` on macOS, `sha256sum` on Linux, or any other tool that supports SHA-256).
2. Upload or run the tool on the downloaded firmware `.bin` file.
3. Open the `checksums.txt` file located in the `Firmware-backup` folder.
4. Copy the checksum value from the `checksums.txt` file.
5. Compare the calculated checksum with the one provided in the `checksums.txt` file. If they match, the firmware file is safe to use.

## Project Structure
- `AirFirmwareDownloader.py`: Main script
- `checksums.json`: File containing expected checksums for different firmware versions
- `Firmware-backup/`: Folder containing pre-downloaded firmware `.bin` files and corresponding checksum files (`checksums.txt`)
- `README.md`: Description file
- `requirements.txt`: List of required libraries

## Notes
- Ensure you have a stable internet connection when downloading files.
- The script creates separate directories for each downloaded firmware version.
- For added safety, always verify the checksum of your firmware files using a checksum tool and compare it with the checksum listed in `checksums.txt`.

## License
This project is available under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or issues, please create a new issue in this repository.
