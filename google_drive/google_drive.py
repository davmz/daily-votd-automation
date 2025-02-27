import os
from google_drive.drive_helper import upload_to_google_drive, retry_failed_uploads

def process_google_drive_uploads(file_path):
    """Main function to handle both new uploads and retry failed uploads."""
    if file_path:
        # Skip upload if file exists locally
        if os.path.exists(file_path):
            print(f"⚠️ Skipping upload: {file_path} already exists locally.")
            return
        
        upload_to_google_drive(file_path)  # Upload new image

    retry_failed_uploads()  # Always check for failed uploads after new ones


# # Example Usage (Called from `main.py`)
# if __name__ == "__main__":
#     process_google_drive_uploads()