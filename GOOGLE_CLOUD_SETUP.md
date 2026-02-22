# Google Cloud Vision AI Setup Guide

## Prerequisites

You need to set up Google Cloud Vision AI for OCR functionality in the Paper Checker feature.

## Step-by-Step Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Note your project ID

### 2. Enable Vision AI API

1. In the Google Cloud Console, navigate to "APIs & Services" > "Library"
2. Search for "Cloud Vision API"
3. Click on "Cloud Vision API" and click "Enable"

### 3. Create Service Account

1. Go to "IAM & Admin" > "Service Accounts"
2. Click "Create Service Account"
3. Give it a name (e.g., "eduVixen-vision-ai")
4. For role, select "Project" > "Editor" or "Cloud Vision AI Service Agent"
5. Click "Create and Continue"
6. Skip granting additional users access
7. Click "Done"

### 4. Generate Service Account Key

1. In the Service Accounts list, click on your newly created service account
2. Go to the "Keys" tab
3. Click "Add Key" > "Create New Key"
4. Select "JSON" format
5. Click "Create"
6. The JSON key file will be downloaded to your computer

### 5. Set Up Authentication

**IMPORTANT**: Never commit the JSON key file to version control!

#### Option A: Environment Variable (Recommended)
1. Upload the JSON key file to your server (keep it secure)
2. Set the environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
   ```

#### Option B: Replit Secrets (for Replit deployment)
1. In Replit, go to your project settings
2. Add a new secret named `GOOGLE_APPLICATION_CREDENTIALS`
3. Copy the entire contents of your JSON key file as the value

### 6. Test the Setup

The Paper Checker will automatically use these credentials when processing uploaded files.

## Cost Information

**Important**: Google Cloud Vision AI is a paid service. Pricing is typically:
- Text Detection: $1.50 per 1,000 images
- Document Text Detection: $1.50 per 1,000 images

Monitor your usage in the Google Cloud Console to avoid unexpected charges.

## Troubleshooting

### Common Issues:

1. **Authentication Error**: Ensure `GOOGLE_APPLICATION_CREDENTIALS` points to the correct JSON file
2. **API Not Enabled**: Make sure Cloud Vision API is enabled in your project
3. **Permissions**: Ensure the service account has the necessary permissions
4. **File Path**: Use absolute paths for the credentials file

### Error Messages:
- "Could not load the default credentials" → Check authentication setup
- "API has not been used" → Enable the Cloud Vision API
- "Permission denied" → Check service account permissions