# Youtube Video Converter - VID2PDF
**Version**: v0.1

## Description
VID2PDF is a desktop application that allows users to convert YouTube and other platform videos into structured PDF documents. This tool processes the content of the video and generates a comprehensive PDF output for improved learning experience and easy referencing.


## Features
- **Multiple Platforms Support: Convert videos from platforms like YouTube and Udemy.
- **User-friendly Interface: Built using TKinter for a simple and intuitive GUI, enhancing user experience.
- **Advanced Processing: Utilizes GC - Video AI and Intelligence, OpenAI, and other state-of-the-art technologies to extract and process video content.
- **Thumbnail Preview: Displays a thumbnail of the selected video for visual confirmation.
- **Progress Tracking: A progress bar keeps users informed about the conversion status.
- **Custom PDF Location: Choose where to save your generated PDF.
- **OCR Integration: Uses Optical Character Recognition (OCR) technology for advanced content extraction.

## Prerequisites
Ensure you have the following libraries and tools installed:
- `tkinter` for GUI
- `requests`
- `BeautifulSoup`
- `PIL` (Pillow)
- `re`
- `yt-dlp` (FLOSS Licensed tool)
- Others specified in `requirements.txt` (if present)

## Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VideoToText/Vid2Text-Transformer.git
   ```

2. Navigate to the cloned directory:

  ```bash
  cd VideoToText
  ```
3. Install required packages:
  ```
  pip install -r requirements.txt
  ```

4. Run the application:
  ```
  python vid_to_pdf.py
  ```

## Usage
- Enter YouTube URL: Paste the link to the YouTube video you wish to convert.
- Set Output Location: Choose where you'd like to save the generated PDF.
- Start: Click the 'Start' button to begin the conversion process. The application will display a thumbnail of the video for confirmation and show conversion progress.
- Enter Video URL: Paste the link to the video from platforms like YouTube or Udemy that you wish to convert.
- Set Output Location: Choose where you'd like to save the generated PDF.
- Start: Click the 'Start' button to begin the conversion process. The application will display a thumbnail of the video for confirmation and show conversion progress.



## Limitations
- The application leverages OCR technology, GC - Video AI, and the GPT-3 turbo model for content extraction and processing. The quality and accuracy of the PDF output might vary based on the clarity, language, and content of the video.

## Developed By:
- 김병주 (201804223)
- 함윤식 (201902769)
- 손제휘 (202102653)
- 하현준 (202102727)
