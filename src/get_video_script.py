import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def youtube_script(gui, url):
    """
    Import YouTube scripts using URL
    """
    result = ""
    service = Service()

    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # Run Chrome on background
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    gui.progress['value'] = 18
    time.sleep(1)
    gui.statusmsg.set(f'Extracting Youtube video script')

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    gui.progress['value'] = 21

    try:
        driver.get(url)

        # Wait for the "More" button to be clickable
        more_selector = "#expand"
        more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, more_selector)))
        gui.progress['value'] = 35
        more_button.click()

        # Wait for the "Open script" button to be clickable
        open_script_selector = "#primary-button > ytd-button-renderer > yt-button-shape > button > yt-touch-feedback-shape > div"
        open_script_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, open_script_selector)))
        gui.progress['value'] = 44
        open_script_button.click()

        idx = 1
        timestamp = time
        process = 44
        while True:
            script_selector = f"#segments-container > ytd-transcript-segment-renderer:nth-child({idx}) > div > yt-formatted-string"
            current = time
            try:
                if timestamp + 1 < current and process < 60:
                    timestamp = current
                    process += 1
                    gui.progress['value'] = process

                script_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, script_selector)))
                result += (script_element.text + " ")
                idx += 1
            except:
                print("All scripts were successfully imported.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        gui.progress['value'] = 60
        driver.quit()
