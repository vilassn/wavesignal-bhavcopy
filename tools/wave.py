import platform
import requests
import zipfile
import tarfile
import os
import subprocess
import time

# Get the system's operating system name
os_name = platform.system()

# Define a dictionary of URLs for each operating system
os_urls = {
    "Windows": [
        'https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_windows-x64_bin.zip',
        'https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_windows-x64_bin-sdk.zip'
    ],
    "Linux": [
        'https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-x64_bin.tar.gz',
        'https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_linux-x64_bin-sdk.tar.gz'
    ],
    "Darwin": [
        'https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_macos-x64_bin.tar.gz',
        'https://download.java.net/java/GA/javafx21.0.1/e5ab43c6aed54893b0840c1f2dcfca4d/GPL/openjfx-21.0.1_macos-x64_bin-sdk.tar.gz'
    ]
}

# Define a dictionary to map OS names to commands
os_commands = {
    "Linux": [
        "runtime/linux/jdk/bin/java",
        "--module-path", "runtime/linux/jfx/lib",
        "--add-modules", "javafx.controls,javafx.fxml,javafx.web",
        "-jar", "runtime/bin/wave"
    ],
    "Windows": [
        "start", "runtime\\win\\jdk\\bin\\javaw.exe",
        "--module-path", "runtime\\win\\jfx\\lib",
        "--add-modules", "javafx.controls,javafx.fxml,javafx.web",
        "-jar", "runtime\\bin\\wave"
    ],
    "Darwin": [
        # Add macOS-specific commands here if needed
    ]
}

def download_and_extract(url, destination_folder):
    for file_url in url:
        # Define a local file name for the downloaded file
        local_file = os.path.join(destination_folder, os.path.basename(file_url))
        print(f"local filename: {local_file}")

        # Send an HTTP GET request to the URL and save the content to a local file
        response = requests.get(file_url)
        with open(local_file, 'wb') as file:
            file.write(response.content)

        # Determine the type (jdk or jfx)
        extract_folder = os.path.join(destination_folder, 'jdk' if 'openjdk' in file_url else 'jfx')

        # Extract the contents based on the file extension
        if file_url.endswith('.zip'):
            with zipfile.ZipFile(local_file, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
        elif file_url.endswith('.tar.gz') or file_url.endswith('.tar'):
            with tarfile.open(local_file, 'r:*') as tar:
                tar.extractall(extract_folder)

        # Clean up by deleting the downloaded file
        os.remove(local_file)

def main():
    print(f"This computer is running {os_name}.")
    # Download java runtime
    if os_name in os_urls:
        print(f"Downloading java runtime for {os_name}.")
        download_urls = os_urls[os_name]
        destination_folder = 'runtime'
        os.makedirs(os.path.join(destination_folder, 'jdk'), exist_ok=True)
        os.makedirs(os.path.join(destination_folder, 'jfx'), exist_ok=True)
        download_and_extract(download_urls, destination_folder)

    # Launch wav
    if os_name in os_commands:
        print(f"Launching wavesignal on {os_name}.")
        # Run the corresponding command
        subprocess.Popen(os_commands[os_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        # Add a sleep of 3 seconds
        time.sleep(3)
    else:
        print(f"This computer is running {os_name}, which is not specifically identified.")

if __name__ == "__main__":
    main()
