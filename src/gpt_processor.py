import os
import openai

def setup_gpt():
    """
    Initialize the OpenAI GPT API with the key.
    """
    api_key = ""
    print(f"Loaded API Key: {api_key}")
    openai.api_key = api_key

def process_video_contents_with_gpt(script_data, ocr_data):
    """
    Given paths to txt files containing voice and OCR data from a video,
    use the GPT API to structure and refine it.
    """
    prompt_content = f"Voice Data: {script_data}\nOCR Data: {ocr_data}\n주요 키워드와 문단을 나눠서 구조화해줘."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_content}
        ]
    )
    
    refined_text = response['choices'][0]['message']['content'].strip()
    return refined_text

# setup_gpt()
# structured_output = process_video_contents_with_gpt("안녕하세요", "test.txt")
# print(structured_output)
