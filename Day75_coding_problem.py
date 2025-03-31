# ✅ Day 75: File Upload API with AWS S3
# --------------------------------------------------------------
# 👉 Task: Create an API to upload and retrieve files from AWS S3.

# 🎯 Problem Statement:
# 🔥 API Endpoints:
# - POST /upload/ → Upload a file
# - GET /files/{filename}/ → Retrieve file URL

# 🎉 Expected Input (Upload):
"""
{
  "file": "my_document.pdf"
}
"""

# 🎉 Expected Output:
"""
{
  "file_url": "https://s3.amazonaws.com/bucket_name/my_document.pdf"
}
"""
# -----------------------------------------------------------------