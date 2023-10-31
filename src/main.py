from video_converter import download_video_from_url
from text_extractor import extract_text_from_video
from audio_transcriber import transcribe_audio_from_video
from gpt_processor import process_text_with_gpt
from pdf_generator import generate_pdf_from_text

def main():
    url = input("Enter the video URL: ")
    video_path = download_video_from_url(url)
    video_text = extract_text_from_video(video_path)
    audio_text = transcribe_audio_from_video(video_path)
    combined_text = video_text + "\n" + audio_text
    refined_text = process_text_with_gpt(combined_text)
    generate_pdf_from_text(refined_text, "output.pdf")
    
if __name__ == "__main__":
    main()
