import hashlib
import requests
import os
import json
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True) 

# Stałe
ASCII_ART = r"""
    _    _      _____ _                                      ____  _     
   / \  (_)_ __|  ___(_)_ __ _ __ _____      ____ _ _ __ ___|  _ \| |    
  / _ \ | | '__| |_  | | '__| '_ ` _ \ \ /\ / / _` | '__/ _ \ | | | |    
 / ___ \| | |  |  _| | | |  | | | | | \ V  V / (_| | | |  __/ |_| | |___ 
/_/   \_\_|_|  |_|   |_|_|  |_| |_| |_|\_/\_/ \__,_|_|  \___|____/|_____| 
"""
BASE_URL = "http://twsfota.198509.xyz/tws_fota_bin/S505/AB1562AE/S505_cc%20ultra_AB1562AE_V310.6.505."
AVAILABLE_VERSIONS = {
    '153': 'Version 153 is available.',
    '152': 'Version 152 is available.',
    '135': 'Version 135 is available.',
    '133': 'Version 133 is available.'
}

def print_ascii_welcome():
    """Print ASCII art and a welcome message."""
    print(Fore.CYAN + ASCII_ART)
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)

def calculate_sha256(file_path):
    """Calculate SHA-256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def download_file(url, file_path, version):
    """Download a file from a URL with a progress bar."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        if total_size == 0:
            print(Fore.RED + Style.BRIGHT + f"Cannot determine size of the file from URL: {url}")
            return False
        
        short_name = f"V{version}"
        with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, 
                  desc=short_name, bar_format='{l_bar}{bar} | {n_fmt}/{total_fmt}', 
                  colour='cyan') as bar:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        bar.update(len(chunk))
        
        return True
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + Style.BRIGHT + f"Error downloading file from {url}: {e}")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"An unexpected error occurred: {e}")
    return False

def load_checksums(json_file):
    """Load checksums from a JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def compare_checksums(version, left_sha256, right_sha256, checksums):
    """Compare calculated checksums with expected checksums."""
    expected = checksums.get(str(version), {"left": None, "right": None})
    return {
        "left_file_checksum": left_sha256,
        "right_file_checksum": right_sha256,
        "left_match": left_sha256 == expected.get("left"),
        "right_match": right_sha256 == expected.get("right")
    }

def print_comparison_results(results):
    """Print comparison results in a formatted manner."""
    print(Fore.GREEN + Style.BRIGHT + "\nChecksum Comparison Results:")
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)
    print(Fore.GREEN + Style.BRIGHT + f"Left file checksum:  {results['left_file_checksum']}")
    print(Fore.GREEN + Style.BRIGHT + f"Right file checksum: {results['right_file_checksum']}")
    print(Fore.GREEN + Style.BRIGHT + f"Left file match:     {'Match' if results['left_match'] else 'No match' if results['left_match'] is not None else 'Not available'}")
    print(Fore.GREEN + Style.BRIGHT + f"Right file match:    {'Match' if results['right_match'] else 'No match' if results['right_match'] is not None else 'Not available'}")
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)

def construct_file_path(version, file_type):
    """Construct the file path for the given version and file type."""
    return os.path.join(
        os.getcwd(), 
        version, 
        os.path.basename(f"{BASE_URL}{version}_fota/S505_cc%20ultra_AB1562AE_V310.6.505.{version}_{file_type}_FotaPackage.bin")
    )

def main():
    """Main function to run the program."""
    print_ascii_welcome()
    checksums = load_checksums('checksums.json')

    while True:
        try:
            version_input = input(Fore.YELLOW + Style.BRIGHT + "Enter the firmware version (last digits, e.g., 153), or press Enter to display available versions: ").strip()

            if not version_input:
                print(Fore.YELLOW + Style.BRIGHT + "\nAvailable Versions:")
                for v in sorted(AVAILABLE_VERSIONS.keys(), reverse=True):
                    print(Fore.GREEN + Style.BRIGHT + f"{AVAILABLE_VERSIONS[v]}")
                
                print(Fore.YELLOW + Style.BRIGHT + "\nPlease enter the firmware version you want to download (e.g., 153): ")
                version_input = input().strip()
            
            if not version_input or version_input not in AVAILABLE_VERSIONS:
                print(Fore.RED + Style.BRIGHT + "Invalid version provided. Exiting...")
                return

            version = version_input
            version_folder = os.path.join(os.getcwd(), version)
            left_file_path = construct_file_path(version, "left")
            right_file_path = construct_file_path(version, "right")

            if os.path.exists(version_folder) and os.path.isfile(left_file_path) and os.path.isfile(right_file_path):
                print(Fore.GREEN + Style.BRIGHT + f"Version {version} is already downloaded.")
                left_sha256 = calculate_sha256(left_file_path)
                right_sha256 = calculate_sha256(right_file_path)
                results = compare_checksums(version, left_sha256, right_sha256, checksums)
                print_comparison_results(results)
                break

            os.makedirs(version_folder, exist_ok=True)

            left_file_url = f"{BASE_URL}{version}_fota/S505_cc%20ultra_AB1562AE_V310.6.505.{version}_left_FotaPackage.bin"
            right_file_url = f"{BASE_URL}{version}_fota/S505_cc%20ultra_AB1562AE_V310.6.505.{version}_right_FotaPackage.bin"

            left_file_path = os.path.join(version_folder, os.path.basename(left_file_url))
            right_file_path = os.path.join(version_folder, os.path.basename(right_file_url))

            print(Fore.CYAN + Style.BRIGHT + "Downloading files...")
            left_downloaded = download_file(left_file_url, left_file_path, version)
            right_downloaded = download_file(right_file_url, right_file_path, version)

            if left_downloaded and right_downloaded:
                print(Fore.GREEN + Style.BRIGHT + "\nFiles downloaded successfully!")
                left_sha256 = calculate_sha256(left_file_path)
                right_sha256 = calculate_sha256(right_file_path)
                results = compare_checksums(version, left_sha256, right_sha256, checksums)
                print_comparison_results(results)
            else:
                print(Fore.RED + Style.BRIGHT + "Failed to download one or both files.")
            
            break
                
        except KeyboardInterrupt:
            print(Fore.RED + Style.BRIGHT + "\nProcess interrupted by user.")
            return
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f"An unexpected error occurred: {e}")
            return

if __name__ == "__main__":
    main()
