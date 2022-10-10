import csv
import time
import pandas as pd
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/chromedriver")
driver.get("https://seawork.com/newfront/marketplace/exhibitors?limit=8")
driver.maximize_window()
time.sleep(20) 

dry = driver.find_elements(By.CLASS_NAME,'MuiBox-root.css-166leeq')
li= []
for i in dry:
    print(i.text)
    
    t1 = i.text
    t2 = t1.lower()
    t3 = t2.replace(" ","-")
    t3 = t3.replace(".","-")
    print(t3)
    li.append(t3)
    # print('===================================================')
Description_1 = []
Address_1 = []
webside_url_1 = []
Representative_1 = []
Tel_phone_1 = []
count = 0
for l in li:

    count += 1
    driver.get(f"https://seawork.com/newfront/exhibitor/{l}");time.sleep(5)
    driver.maximize_window()
    try:
         # WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="__next"]/div[2]/div[1]/main/div/div/div[3]/div/div[2]/div[2]/div[{i}]/div/div[1]/div[2]/div[1]/div[1]/h3/div'))).click()
        # WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'css-1vg7hqh'))).click()
        try:
            print('===================================================')
            Description = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.dangerouslyHtml.css-1n5ipg9')))
            print(Description.text)
            Description_1.append(Description.text)
        except:
            print('NON')
            Description_1.append("None")
            pass
        try:
            
            Address = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.MuiTypography-alignCenter.MuiTypography-gutterBottom.css-1m4psc1')))
            Address_1.append(Address.text)
            print(Address.text)
        except:
            Address_1.append("None")
            print('NON')
            pass
        try:
            webside_url = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'MuiTypography-root.MuiTypography-subtitle2.MuiTypography-noWrap.css-9lz1ji')))
            webside_url_1.append(webside_url.text)
            print(webside_url.text)
        except:
            webside_url_1.append("None")
            print('NON')
            pass
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN);time.sleep(3)
        try:
            Representative = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,'MuiTypography-root.MuiTypography-h4.MuiTypography-alignCenter.MuiTypography-noWrap.pointer.css-15pu307')))
            Representative_1.append(Representative.text)
            print(Representative.text)
        except:
            Representative_1.append("None")
            print('NON')
            pass
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN);time.sleep(3)
        try:
            Tel_phone = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="matchmaking_information"]/div/div/div/div/p')))
            Tel_phone_1.append(Tel_phone.text)
            print(Tel_phone.text)
            time.sleep(6)
            print('===================================================')
        except:
            print('NON')
            Tel_phone_1.append("None")
            pass 
    except:
        print('NON')
        pass

    if count == 10:
        break

dict_out ={
    'Company':li,
    'Description':Description_1,
    'Address':Address_1,
    'webside_url':webside_url_1,
    'Representative':Representative_1,
    'Tel_phone':Tel_phone_1,
}

print(dict_out)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
df = pd.DataFrame(dict_out)
print(df)
df.to_csv('data.csv')