import re
import webvtt


def remove_timeline(vtt_string):
    # Use regular expression pattern to remove timeline information
    pattern = r"(\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3})"
    result = re.sub(pattern, "", vtt_string)
    return result


def vtt_to_string(script_path):
    """
    Convert Script to String
    """
    try:
        with open(script_path, 'r') as file:
            vtt_string = file.read()
            vtt_string_without_timeline = remove_timeline(vtt_string)
            captions = webvtt.read_buffer(vtt_string_without_timeline)
            result = ""
            prev_text = ""
            for caption in captions:
                text = caption.text.strip()
                if text != prev_text:  # Add only if different from the previous string
                    result += text
                    prev_text = text
            return result
    except FileNotFoundError:
        print(f"File not found at path: {script_path}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


path = "C:/Users/sonjh/OneDrive/바탕 화면/Python YouTube API Tutorial： Using OAuth to Access User Accounts.ko.vtt"
s = vtt_to_string(path)
print(s)
