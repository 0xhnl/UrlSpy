# UrlSpy

## Overview
UrlSpy is a powerful tool designed to extract URL paths from a given input file. It simplifies the process of identifying and analyzing various URL patterns, making it an essential utility for developers, cybersecurity analysts, and anyone working with web data.

## Features
- **URL Extraction:** Efficiently extracts URLs from an input file, including HTTP and HTTPS links.
- **Protocol Support:** Supports multiple protocols like HTTP, HTTPS, FTP, SFTP, and more.
- **Output Formatting:** Displays extracted URLs in a user-friendly format for easy analysis.
- **Customizable Options:** Allows users to specify filters and search parameters for extraction.

## Requirements
- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4` (if applicable)

## Installation
Clone the repository:
```bash
git clone https://github.com/0xhnl/UrlSpy.git
cd UrlSpy
python3 UrlSpy.py
```

## Usage
To extract URLs from an input file, use the following command:
```bash
$ python3 UrlSpy.py
usage: UrlSpy.py [-h] -i INPUT [-o OUTPUT]
UrlSpy.py: error: the following arguments are required: -i/--input

$ python3 UrlSpy.py -i domain.txt -o extracted_urls.txt
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes or enhancements.
