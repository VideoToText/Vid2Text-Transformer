from video_converter import download_video_from_url
from text_extractor import extract_text_from_video
from audio_transcriber import transcribe_audio_from_video
from gpt_processor import process_video_contents_with_gpt, setup_gpt
from pdf_generator import generate_pdf_from_text

def main():
    # Set up the GPT API
    setup_gpt()

    url = input("Enter the video URL: ")
    video_path = download_video_from_url(url)
    video_text = extract_text_from_video(video_path)
    audio_text = transcribe_audio_from_video(video_path)
    structured_output = process_video_contents_with_gpt(audio_text, video_text)
    generate_pdf_from_text(structured_output, "output.pdf")
    
if __name__ == "__main__":
    main()
