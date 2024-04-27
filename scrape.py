from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def automateFetch(image_url:str, save_directory:str = "images"):
    os.makedirs(save_directory, exist_ok=True)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)


    driver.get(image_url)
    img_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img"))
    )

    time.sleep(1)
    image_filename = save_directory  + str(hash(image_url)) + ".png"

    with open(os.path.join(save_directory, image_filename), "wb") as f:
        f.write(img_element.screenshot_as_png)

    print(f"Image saved as {os.path.join(save_directory, image_filename)}")

    driver.quit()
