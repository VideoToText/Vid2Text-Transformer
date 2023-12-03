import os
import time

import openai

def setup_gpt():
    """
    Initialize the OpenAI GPT API with the key.
    """
    api_key = ""
    print(f"Loaded API Key: {api_key}")
    openai.api_key = api_key

def save_text_to_file(filename, data):
    """
    Save the given data to a text file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def read_file(filename):
    """
    Read and return the content of the specified file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def process_video_contents_with_gpt(script_data, ocr_data):
    """
    Given paths to txt files containing voice and OCR data from a video,
    use the GPT API to structure and refine it.
    """

    prompt_content = f"Voice Data: {script_data}\nOCR Data: {ocr_data}\n The above is a transcript of a video. Please structure it into a well-formatted document starting with indexes like a textbook."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_content}
        ]
    )

    time.sleep(1)
    
    refined_text = response['choices'][0]['message']['content'].strip()
    print("refined_txt: ", refined_text)
    
    gpt_filename = './gpt.txt'
    save_text_to_file(gpt_filename, refined_text)
    return refined_text

setup_gpt()
process_video_contents_with_gpt(read_file('./script_data.txt'), read_file('./ocr_data.txt'))
