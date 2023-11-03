# Youtube Video Converter - VID2PDF
**Version**: v0.1

## Description
VID2PDF is a desktop application that allows users to convert YouTube videos into PDFs. This tool fetches the content of the video and processes it, creating a structured PDF output for easy reading and reference.

## Features
- **User-friendly Interface**: Simple and intuitive GUI for easy operation.
- **Thumbnail Preview**: Displays a thumbnail of the selected YouTube video for visual confirmation.
- **Progress Tracking**: A progress bar keeps users informed about the conversion status.
- **Custom PDF Location**: Choose where to save your generated PDF.

## Prerequisites
Ensure you have the following libraries and tools installed:
- `tkinter`
- `requests`
- `BeautifulSoup`
- `PIL` (Pillow)
- `re`
- Others specified in `requirements.txt` (if present)

## Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VideoToText/Vid2Text-Transformer.git
   ```

2. Navigate to the cloned directory:

  ```bash
  cd YOUR_REPO_NAME
  ```
3. Install required packages:
  ```
  pip install -r requirements.txt
  ```

4. Run the application:
  ```
  python main.py
  ```

## Usage
- Enter YouTube URL: Paste the link to the YouTube video you wish to convert.
- Set Output Location: Choose where you'd like to save the generated PDF.
- Start: Click the 'Start' button to begin the conversion process. The application will display a thumbnail of the video for confirmation and show conversion progress.

## Limitations
- This application relies on extracting content from YouTube videos and processing the content using the GPT model. The quality of the PDF output may vary based on the video content and clarity of speech.

## Developed By:
- 김병주 (201804223)
- 함윤식 (201902769)
- 손제휘 (202102653)
- 하현준 (202102727)

