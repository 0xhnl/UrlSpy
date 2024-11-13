import re
import argparse
import requests

def extract_urls(filename):
    # Define the URL pattern to match URLs in the file
    url_pattern = re.compile(r"https?://[^\s]+|ftp://[^\s]+|ftps://[^\s]+|sftp://[^\s]+|scp://[^\s]+|rsync://[^\s]+|webdav://[^\s]+|mtpp://[^\s]+|p2p://[^\s]+|dcc://[^\s]+|nat-pmp://[^\s]+|cpio://[^\s]+|zfs://[^\s]+|dc://[^\s]+|tus://[^\s]+|btsync://[^\s]+|at://[^\s]+|xfs://[^\s]+|hdfs://[^\s]+|bt://[^\s]+|icap://[^\s]+|openvpn://[^\s]+|nfs4://[^\s]+|webrtc://[^\s]+|http2://[^\s]+|ipfs://[^\s]+|bittorrent://[^\s]+")
    extracted_urls = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                urls = url_pattern.findall(line)
                extracted_urls.extend(urls)

        return extracted_urls

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return []

def fetch_and_extract_http_endpoints(url):
    try:
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()
        # Find all HTTP/HTTPS links in the page source
        endpoint_pattern = re.compile(r"https?://[^\s\"'>]+|ftp://[^\s\"'>]+|sftp://[^\s\"'>]+|ftps://[^\s\"'>]+|file://[^\s\"'>]+|tftp://[^\s\"'>]+")
        endpoints = endpoint_pattern.findall(response.text)
        return endpoints
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Extract HTTP/HTTPS endpoints from the source of URLs in a file.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file containing URLs")
    parser.add_argument("-o", "--output", type=str, help="Output file to save extracted URLs")
    args = parser.parse_args()

    # Step 1: Extract URLs from the file
    urls = extract_urls(args.input)
    if not urls:
        print("No URLs found in the input file.")
        return

    extracted_results = []

    # Step 2: For each URL, fetch the page source and extract HTTP endpoints
    for url in urls:
        print(f"\nChecking URL: {url}")
        endpoints = fetch_and_extract_http_endpoints(url)
        if endpoints:
            print("Extracted HTTP/HTTPS endpoints:")
            for endpoint in endpoints:
                output_line = f"[{endpoint}] [{url}]"
                print(output_line)
                extracted_results.append(output_line)
        else:
            print("No HTTP/HTTPS endpoints found.")

    # Write to output file if specified
    if args.output:
        with open(args.output, 'w') as outfile:
            for line in extracted_results:
                outfile.write(line + '\n')
        print(f"Extracted URLs saved to {args.output}")

if __name__ == "__main__":
    main()
