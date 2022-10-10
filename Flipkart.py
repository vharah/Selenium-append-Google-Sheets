
#shoes data from flipkart

from selenium import webdriver
import pandas as pd
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")

txt = "flipkart"

# driver.find_element(By.ID,'input').send_keys(txt)
driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').send_keys(txt)
time.sleep(2)
driver.find_element(By.CLASS_NAME,'gNO89b').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'TbwUpd.NJjxre').click()
# time.sleep(2)
driver.find_element(By.CLASS_NAME,'_2KpZ6l._2doB4z').click()
# time.sleep(2)

sh = "Laptop"
driver.find_element(By.CLASS_NAME,'_3704LK').send_keys(sh)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'L0Z3Pu').click()
time.sleep(2)


names = []
Brand = []
prices = []
product_discount_list = []
ratings = []

# acer Aspire Ryzen 5 Quad Core 3500U - (8 GB/512 GB SSD/Windows 11 Home) A315-23 Laptop  (15.6 inch, Charcoal Black, 1.9 kg)
# ₹34,890
# 4.2

divs = driver.find_elements(By.CLASS_NAME,'_3pLy-c.row')

for i in divs:
    i.click()
    time.sleep(3)

  
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    



    name = driver.find_element(By.CLASS_NAME,'B_NuCI')
    time.sleep(2)
    names.append(name.text)
    # name.text.split[' ',1]
    # print(name.text)
    Brand = name.text.split(' ',1)[0]
    # Brand.append(Brand)
    # print(Brand)



    price = driver.find_element(By.CLASS_NAME,'_30jeq3._16Jk6d').text
    # print(price)
    prices.append(price)
    time.sleep(2)

    product_discount = driver.find_element(By.CLASS_NAME,'_3I9_wc._2p6lqe')
    product_discount_list.append(product_discount.text)
    # print(product_discount_list)

    try:

        rating = driver.find_element(By.CLASS_NAME,'_3LWZlK')
        ratings.append(rating.text)
        # print(rating)
        
    except:
        ratings.append("NaN")
        # print("NaN")


    driver.close()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)



data = {
    'Shoes Name' : names,
    'Brand': Brand,
    'Price' : prices,
    'product discount': product_discount_list,
    'Rating' : ratings
}

df = pd.DataFrame.from_dict(data)

# print(df)
# df = df.transpose()
df.to_csv("data.csv")

driver.close()