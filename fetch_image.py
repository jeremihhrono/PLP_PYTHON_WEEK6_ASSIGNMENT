import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    print("Ubuntu Image Fetcher - 'I am because we are'")
    
    # Prompt user for image URL
    image_url = input("Please enter the URL of the image you'd like to fetch: ").strip()

    # Validate URL
    if not image_url.lower().startswith(('http://', 'https://')):
        print("❌ Invalid URL. Please enter a valid http:// or https:// URL.")
        return

    # Create directory
    image_dir = "Fetched_Images"
    os.makedirs(image_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Raise exception for bad responses (4xx, 5xx)

        # Extract or generate filename
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            # Fallback filename
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"image_{timestamp}.jpg"

        # Full path to save
        image_path = os.path.join(image_dir, filename)

        # Save image in binary mode
        with open(image_path, 'wb') as file:
            file.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {image_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching image: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
