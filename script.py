import csv
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from google.oauth2 import service_account
from selenium.webdriver.common.by import By
from googleapiclient.discovery import build
from selenium.webdriver.common.keys import Keys
from google.oauth2.credentials import Credentials


'''GOOGLE SHEET'''
SAMPLE_SPREADSHEET_ID = "1hierP5fo2qUO4pscxQCQbx2edv_tmEE_FO7X94Ts0hk"

SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]

SERVICE_ACCOUNT_FILE = "/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/cred1.json"

FILE_PATH = "/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/product.csv"

CREDS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPE)
''' SELENIUM '''
driver = webdriver.Chrome(executable_path="/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/chromedriver")
driver.get("https://www.google.com/")
driver.maximize_window()

search_flipkart = driver.find_element(By.NAME,'q')
search_flipkart.send_keys('flipkart')
time.sleep(2)
search_flipkart.send_keys(Keys.ENTER)
time.sleep(3)
click_flipkart = driver.find_element(By.CLASS_NAME,'MBeuO').click()
time.sleep(3)
try:
    pop_up = driver.find_element(By.CLASS_NAME,'_2doB4z').click()
except Exception as e:
    print(e)
time.sleep(5)


RECORDS =[]

search_product = driver.find_element(By.NAME,'q')
search_product.send_keys('laptops')
search_product.send_keys(Keys.ENTER)
time.sleep(2)

product_name = driver.find_elements(By.CLASS_NAME,'_4rR01T')
product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
# print(len(product_name_list))

product_price = driver.find_elements(By.CLASS_NAME,'_1_WHN1')
product_price_list = []
for i in product_price:
    price = i.text
    product_price_list.append(price)
# print(len(product_price_list))
time.sleep(5)

product_rating = driver.find_elements(By.CLASS_NAME,'_3LWZlK')
product_rating_list = []
for i in product_rating:
    rating = i.text
    product_rating_list.append(rating)
# print(len(product_rating_list))
time.sleep(5)

original_product_price = driver.find_elements(By.CLASS_NAME,'_27UcVY')
original_product_price_list = []
for i in original_product_price:
    original_price = i.text
    original_product_price_list.append(original_price)
# print(original_product_price_list)
time.sleep(5)

product_discount = driver.find_elements(By.CLASS_NAME,'_3Ay6Sb')
product_discount_list = []
for i in product_discount:
    dis = i.text
    product_discount_list.append(dis)
# print(len(product_discount_list))

ALL_RECORDS = []
n = len(product_name_list)
for i in range(n):
    ALL_RECORDS.append([product_name_list[i],product_price_list[i],original_product_price_list[i],product_rating_list[i],product_discount_list[i]])
# print(ALL_RECORDS)
''' DATA FRAME '''

df = pd.DataFrame(ALL_RECORDS,columns=["Product_Name","Product_Price","Product_Original_Price","Product_Rating","Product_Discount"])
CONVERT_DF_LIST_OF_LIST = df.values.tolist()

service = build('sheets', 'v4',credentials=CREDS)
sheet = service.spreadsheets()
request = sheet.values().update(spreadsheetId = SAMPLE_SPREADSHEET_ID, range= "Sheet1", 
        valueInputOption="USER_ENTERED", body={"values":CONVERT_DF_LIST_OF_LIST}).execute()