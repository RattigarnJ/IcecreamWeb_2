from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
import time
import requests
import os
import math
import sys
import io

# New Task
# Select Period
# By get period_count from app by calculation of APP.py

# sys.argv[1] tr first day
# sys.argv[2] td first day
# sys.argv[3] month
# sys.argv[4] year
# sys.argv[5] period day

# ???
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")

chrome_options = Options()
# chrome_options.add_argument("--headless")  
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# EDIT PATH for keep images and files
BASE_SAVE_PATH = os.path.join(os.path.expanduser("~"), "Documents", "IceCreamDetection" , "LyingdownContract")

# CSV keep
# EDIT NAME ? (-)
name_csv = "CSV_file" 
# EDIT NAME ? (-)
name_image = "IMAGE_file"

download_folder_csv = os.path.join(BASE_SAVE_PATH, name_csv)
download_folder_image = os.path.join(BASE_SAVE_PATH, name_image)
os.makedirs(download_folder_csv, exist_ok=True)  
os.makedirs(download_folder_image, exist_ok=True) 

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": f"{download_folder_csv}",
    "download.prompt_for_download": False,
    "directory_upgrade": True
})

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

def get_max_pages():
    # Pull XPATH ALL ROWS
    rows_ALL = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/div')
    rows_text = rows_ALL.text.strip()  
    index_of_of = rows_text.find('of')
    rows_count = float(rows_text[index_of_of + 2:].strip())

    # Split Text back 'of'
    rows_count = float(rows_text.split('of')[-1].strip())  
    pages_pp = math.ceil(rows_count / 10)  
    print(pages_pp)
    return pages_pp

try:
    # Open Website
    driver.get("https://pm-rsm.cpretailink.co.th/login")
    output_dir = download_folder_image

    # Put Username & Password then Enter Login
    username_user = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div/div/div[2]/form/div[1]/input')
    password_user = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div/div/div[2]/form/div[2]/div/input')

    #   Edit username & password here !!
    username_put = 'benjaponsuns'
    password_put = 'Benjapon@0125'

    username_user.send_keys(username_put)
    password_user.send_keys(password_put)

    password_user.send_keys(Keys.RETURN)
    time.sleep(2)

    # Select Part of year you want to check
    selecting_part = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[1]/div[2]/mat-form-field/div[1]/div[2]/div[1]/input')
    selecting_part.click()
    time.sleep(2)

    year_put = int(sys.argv[4])
    # year_put = 2025

    if year_put == 2023:
        year_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[2]/button/div[1]')
        year_select.click()
        time.sleep(2)
    elif year_put == 2024:
        year_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[3]/button/div[1]')
        year_select.click()
        time.sleep(2)
    elif year_put == 2025:
        year_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[4]/button/div[1]')
        year_select.click()
        time.sleep(2)

    month_put = int(sys.argv[3])
    # month_put = 2

    month_table = {1: [2,1], 2: [2,2], 3: [2,3], 4: [2,4], 5: [3,1], 6: [3,2], 7: [3,3], 8: [3,4], 9: [4,1], 10: [4,2], 11: [4,3], 12: [4,4]}
    month_select = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-year-view/table/tbody/tr[{month_table[month_put][0]}]/td[{month_table[month_put][1]}]/button')
    month_select.click()
    time.sleep(2)

    # STATIC PART # START

    # Select ALL from search from
    search_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[2]/div[2]/mat-button-toggle-group/mat-button-toggle[4]/button/span')
    search_select.click()
    time.sleep(2)

    # Select Company part
    cpn_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[3]/div[2]/app-multi-search-box/div/input')
    cpn_select.click()
    time.sleep(5)

    cpn_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[1]/div')
    cpn_select.click()
    time.sleep(2)

    seven_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[2]/div[3]/div[2]/ul/li[1]/label')
    seven_select.click()
    time.sleep(2)

    finish_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[1]/button')
    finish_button.click()
    time.sleep(2)

    # Select Contract type
    contract_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[4]/div[2]/app-multi-search-box/div/input')
    contract_select.click()
    time.sleep(2)

    contract_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[1]/div')
    contract_select.click()
    time.sleep(2)

    downicy_contract = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[2]/div[3]/div[1]/input")
    downicy_contract.send_keys("ทรงนอน")
    time.sleep(2)

    downicy_contract = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[2]/div[3]/div[3]/ul/li')
    downicy_contract.click()
    time.sleep(2)

    finish_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[1]/button')
    finish_button.click()
    time.sleep(2)

    # Select search
    search_button = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[7]/button')
    search_button.click()
    time.sleep(5)

    tr = int(sys.argv[1])
    td = int(sys.argv[2])

    # start day 
    # tr = 1
    # td = 7

    period_day = (int(sys.argv[5])) + 1
    # period_day = 1

    # Var downloaded_urls
    downloaded_urls = set() 

    # Var parameter
    current_page = 1
    next_count = 1
    i = 1
    count_row_now = 0
    current_day = 1

    # When not end
    while current_day <= period_day:
        try: 
            # Switch to New Tab for next processing
            driver.switch_to.window(driver.window_handles[1])

            if td > 7:
                td == 1
                tr += 1

            if tr > 5:
                tr == 1

            # IN CASE - rpa didnt see element
            if tr <= 2:
                # Just click
                day_xpath = f'/html/body/app-root/app-e-service-plan/div/full-calendar/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[{tr}]/td[{td}]/div/div[2]/div[1]/a'
                driver.find_element(By.XPATH, day_xpath).click()
                time.sleep(2)
            elif tr > 2:
                # Scroll Down for show element
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                day_xpath = f'/html/body/app-root/app-e-service-plan/div/full-calendar/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[{tr}]/td[{td}]/div/div[2]/div[1]/a'
                driver.find_element(By.XPATH, day_xpath).click()
                time.sleep(2)

            # Click excel button for downloading csv file
            csv_click = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/div/div[2]/div/button')
            csv_click.click()
            time.sleep(5)

            # max pages should fill by Total of pages that calculated
            max_pages = get_max_pages()

            # Pull XPATH ALL ROWS
            rows_ALL = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/div')
            rows_text = rows_ALL.text.strip()  
            index_of_of = rows_text.find('of')
            rows_count = float(rows_text[index_of_of + 2:].strip())

            # Split Text back 'of'
            rows_count = float(rows_text.split('of')[-1].strip())
            print(f"มีจำนวนแถวทั้งหมด {rows_count}")

            # Just Day
            # Not finish Page
            while current_page <= max_pages:
                try:
                    total_rows = len(driver.find_elements(By.XPATH, '//app-table-contract/div/table/tbody/tr'))
                    print(f"พบหัวข้อทั้งหมด {total_rows} รายการในหน้า {current_page}")

                    # Split Date
                    name_file = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/div/div[1]')
                    name_file_text = name_file.text.strip()
                    date = name_file_text.split("PM")[1].strip()

                    # Find lasest file in folder csv
                    files = os.listdir(download_folder_csv)
                    files.sort(key=lambda x: os.path.getctime(os.path.join(download_folder_csv, x)), reverse=True)
                    latest_file = os.path.join(download_folder_csv, files[0])

                    # Change name file
                    new_filename = os.path.join(download_folder_csv, f"{date}_csv.csv")
                    os.rename(latest_file, new_filename)

                    if current_page == 1:
                        try:
                            # Topic 1 - end
                            for row_index in range(1, total_rows + 1):
                                try:
                                    topic_xpath = f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[5]'
                                    topic_link = driver.find_element(By.XPATH, topic_xpath)

                                    count_row_now += 1
                                    print(f"จำนวนแถวที่ทำไปแล้ว {count_row_now}")

                                    if row_index == rows_count:

                                        if 5 <= row_index <= 10:

                                            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                            time.sleep(3)

                                            # Check 'รหัสร้าน' before Click
                                            number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                            number_store_text = number_store.text.strip()

                                            driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                            topic_link.click()
                                            print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                            time.sleep(5)

                                            # Create Folder of store before Downloading image
                                            os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                            output_dir = f"{download_folder_image}/{date}/{number_store_text}"
                                            
                                            # Find element of Path div
                                            div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                            # Download Picture for keep in folder
                                            # For Using Water Tank
                                            # for div in div_elements_cooler:

                                            #     div_text = div.text
                                            #     # Use text before "ตู้ทรงยืน"
                                            #     number = div_text.split(' ')[0] 

                                            #     # Searching Text "รูปหลังทำ"
                                            #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                                
                                            #     if after_use_div:
                                            #         # Seraching images part "รูปหลังทำ"
                                            #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                            #         for idx, img in enumerate(image_elements):
                                            #             image_url = img.get_attribute("src")
                                            #             if image_url:
                                            #                 # File name
                                            #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                            
                                            #                 response = requests.get(image_url, stream=True)
                                            #                 if response.status_code == 200:
                                            #                     # Downloading image
                                            #                     with open(filename, 'wb') as file:
                                            #                         for chunk in response.iter_content(1024):
                                            #                             file.write(chunk)
                                            #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                            #                 else:
                                            #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            driver.back()
                                            time.sleep(5)

                                            # OVER VALUE for quit loop
                                            current_page += 500

                                        elif row_index < 5:

                                            driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)

                                            # Check 'รหัสร้าน' before Click
                                            number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                            number_store_text = number_store.text.strip()

                                            topic_link.click()
                                            print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                            time.sleep(5)

                                            # Create Folder of store before Downloading image
                                            os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                            output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                            # Find element of Path div
                                            div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                            # Download Picture for keep in folder
                                            # For Using Water Tank
                                            # for div in div_elements_cooler:

                                            #     div_text = div.text
                                            #     # Use text before "ตู้ทรงยืน"
                                            #     number = div_text.split(' ')[0] 

                                            #     # Searching Text "รูปหลังทำ"
                                            #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                                
                                            #     if after_use_div:
                                            #         # Seraching images part "รูปหลังทำ"
                                            #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                            #         for idx, img in enumerate(image_elements):
                                            #             image_url = img.get_attribute("src")
                                            #             if image_url:
                                            #                 # File name
                                            #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                            
                                            #                 response = requests.get(image_url, stream=True)
                                            #                 if response.status_code == 200:
                                            #                     # Downloading image
                                            #                     with open(filename, 'wb') as file:
                                            #                         for chunk in response.iter_content(1024):
                                            #                             file.write(chunk)
                                            #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                            #                 else:
                                            #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            driver.back()
                                            time.sleep(3)

                                            # OVER VALUE for quit loop
                                            current_page += 500

                                    elif 5 <= row_index < 10 and count_row_now < rows_count:

                                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(3)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"
                                        
                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        driver.back()
                                        time.sleep(5)

                                    elif row_index < 5 and row_index < rows_count:

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        driver.back()
                                        time.sleep(3)
                                    
                                    elif row_index == 10 and count_row_now < rows_count:

                                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(3)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        driver.back()
                                        time.sleep(3)

                                        current_page += 1

                                        next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                        next_button.click()
                                        time.sleep(3)
                                        
                                        driver.execute_script("window.scrollTo(0, 0);")
                                        time.sleep(3)

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในหัวข้อที่ {row_index}: {e}")
                                    break

                        except Exception as e:
                            print(f"เกิดข้อผิดพลาด: {e}")

                    if current_page >= 2 and current_page <= max_pages:
                        try:
                            # Topic 1 - end
                            for row_index in range(1, total_rows + 1):
                                try:
                                    topic_xpath = f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[5]'
                                    topic_link = driver.find_element(By.XPATH, topic_xpath)

                                    count_row_now += 1
                                    print(f"จำนวนแถวที่ทำไปแล้ว {count_row_now}")

                                    if (row_index == (rows_count % 10) and count_row_now == rows_count) or count_row_now == rows_count:

                                        if 5 <= row_index <= 10:

                                            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                            time.sleep(3)

                                            # Check 'รหัสร้าน' before Click
                                            number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                            number_store_text = number_store.text.strip()

                                            driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                            topic_link.click()
                                            print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                            time.sleep(5)

                                            # Create Folder of store before Downloading image
                                            os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                            output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                            # Find element of Path div
                                            div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                            # Download Picture for keep in folder
                                            # For Using Water Tank
                                            # for div in div_elements_cooler:

                                            #     div_text = div.text
                                            #     # Use text before "ตู้ทรงยืน"
                                            #     number = div_text.split(' ')[0] 

                                            #     # Searching Text "รูปหลังทำ"
                                            #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                                
                                            #     if after_use_div:
                                            #         # Seraching images part "รูปหลังทำ"
                                            #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                            #         for idx, img in enumerate(image_elements):
                                            #             image_url = img.get_attribute("src")
                                            #             if image_url:
                                            #                 # File name
                                            #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                            
                                            #                 response = requests.get(image_url, stream=True)
                                            #                 if response.status_code == 200:
                                            #                     # Downloading image
                                            #                     with open(filename, 'wb') as file:
                                            #                         for chunk in response.iter_content(1024):
                                            #                             file.write(chunk)
                                            #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                            #                 else:
                                            #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                            driver.back()
                                            time.sleep(3)
                                            
                                            # OVER VALUE for quit loop
                                            current_page += 500

                                        elif row_index < 5:

                                            driver.execute_script("window.scrollTo(0, 0);")
                                            time.sleep(3)

                                            # Check 'รหัสร้าน' before Click
                                            number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                            number_store_text = number_store.text.strip()

                                            driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                            topic_link.click()
                                            print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                            time.sleep(5)

                                            # Create Folder of store before Downloading image
                                            os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                            output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                            # Find element of Path div
                                            div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                            # Download Picture for keep in folder
                                            # For Using Water Tank
                                            # for div in div_elements_cooler:

                                            #     div_text = div.text
                                            #     # Use text before "ตู้ทรงยืน"
                                            #     number = div_text.split(' ')[0] 

                                            #     # Searching Text "รูปหลังทำ"
                                            #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                                
                                            #     if after_use_div:
                                            #         # Seraching images part "รูปหลังทำ"
                                            #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                            #         for idx, img in enumerate(image_elements):
                                            #             image_url = img.get_attribute("src")
                                            #             if image_url:
                                            #                 # File name
                                            #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                            
                                            #                 response = requests.get(image_url, stream=True)
                                            #                 if response.status_code == 200:
                                            #                     # Downloading image
                                            #                     with open(filename, 'wb') as file:
                                            #                         for chunk in response.iter_content(1024):
                                            #                             file.write(chunk)
                                            #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                            #                 else:
                                            #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                            for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                            driver.back()
                                            time.sleep(3)

                                            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                            time.sleep(3)

                                            # OVER VALUE for quit loop
                                            current_page += 500
                                            
                                    elif 5 <= row_index < 10 and count_row_now < rows_count:

                                        # Scrolling Down
                                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(3)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                        driver.back()
                                        time.sleep(3)

                                        for next_count in range(i):
                                            try:
                                                next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                                next_button.click()
                                                time.sleep(3)

                                            except Exception as e:
                                                print(f"เกิดข้อผิดพลาด: {e}")
                                                break

                                    elif row_index < 5 and count_row_now < rows_count:

                                        driver.execute_script("window.scrollTo(0, 0);")
                                        time.sleep(3)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        driver.back()
                                        time.sleep(4)

                                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(3)

                                        for next_count in range(i):
                                            try:
                                                next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                                next_button.click()
                                                time.sleep(3)

                                            except Exception as e:
                                                print(f"เกิดข้อผิดพลาด: {e}")
                                                break

                                        driver.execute_script("window.scrollTo(0, 0);")
                                        time.sleep(3)

                                    elif row_index == 10 and count_row_now < rows_count:

                                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(3)

                                        # Check 'รหัสร้าน' before Click
                                        number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                        number_store_text = number_store.text.strip()

                                        driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                        topic_link.click()
                                        print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                        time.sleep(5)

                                        # Create Folder of store before Downloading image
                                        os.makedirs(f"{download_folder_image}/{date}/{str(number_store_text)}", exist_ok=True)
                                        output_dir = f"{download_folder_image}/{date}/{number_store_text}"

                                        # Find element of Path div
                                        div_elements_cooler = driver.find_elements(By.XPATH, "//div[contains(text(), 'ตู้ไอศกรีม')]")

                                        # Download Picture for keep in folder
                                        # For Using Water Tank
                                        # for div in div_elements_cooler:

                                        #     div_text = div.text
                                        #     # Use text before "ตู้ทรงยืน"
                                        #     number = div_text.split(' ')[0] 

                                        #     # Searching Text "รูปหลังทำ"
                                        #     after_use_div = div.find_elements(By.XPATH, ".//div[contains(text(), 'รูปหลังทำ')]")
                                            
                                        #     if after_use_div:
                                        #         # Seraching images part "รูปหลังทำ"
                                        #         image_elements = after_use_div[0].find_elements(By.XPATH, ".//img")
                                        #         for idx, img in enumerate(image_elements):
                                        #             image_url = img.get_attribute("src")
                                        #             if image_url:
                                        #                 # File name
                                        #                 filename = os.path.join(output_dir, f"{date}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                        #                 response = requests.get(image_url, stream=True)
                                        #                 if response.status_code == 200:
                                        #                     # Downloading image
                                        #                     with open(filename, 'wb') as file:
                                        #                         for chunk in response.iter_content(1024):
                                        #                             file.write(chunk)
                                        #                     print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                        #                 else:
                                        #                     print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        for div in div_elements_cooler:
                                                div_text = div.text
                                                # Use text before "ตู้ทรงยืน"
                                                number = div_text.split(' ')[0] 

                                                # ค้นหาทุก <img> ใน div โดยไม่สนใจ "รูปหลังทำ"
                                                image_elements = div.find_elements(By.XPATH, ".//img")
                                                
                                                for idx, img in enumerate(image_elements):
                                                    image_url = img.get_attribute("src")
                                                    if image_url:
                                                        # File name (ยังคงใช้ "ตู้ทรงนอน" ตามโค้ดเดิม แต่สามารถปรับได้)
                                                        filename = os.path.join(output_dir, f"{number_store_text}_{number}_ตู้ทรงนอน_{idx + 1}.jpg")
                                                        
                                                        response = requests.get(image_url, stream=True)
                                                        if response.status_code == 200:
                                                            # Downloading image
                                                            with open(filename, 'wb') as file:
                                                                for chunk in response.iter_content(1024):
                                                                    file.write(chunk)
                                                            print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                        else:
                                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")

                                        driver.back()
                                        time.sleep(2)
                                        
                                        current_page += 1

                                        for next_count in range(i):
                                            try:
                                                next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                                next_button.click()
                                                time.sleep(3)
                                                
                                            except Exception as e:
                                                print(f"เกิดข้อผิดพลาด: {e}")
                                                break

                                        i += 1

                                        next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                        next_button.click()
                                        time.sleep(5)

                                        driver.execute_script("window.scrollTo(0, 0);")
                                        time.sleep(3)

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาด: {e}")
                        
                        except Exception as e:
                            print(f"เกิดข้อผิดพลาด: {e}")

                except Exception as e:
                    print(f"เกิดข้อผิดพลาด: {e}")

            td += 1
            current_day += 1
            current_page = 1
            next_count = 1
            i = 1
            count_row_now = 0

            driver.back()
            time.sleep(5)
                
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
finally:
    driver.quit()
