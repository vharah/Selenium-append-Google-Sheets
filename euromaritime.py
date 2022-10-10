import csv
import time
import pandas as pd
from time import sleep
from itertools import count
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="/home/zec/Desktop/Python File/selenium_flipkart_data_&_append_data_gsheet/chromedriver")
driver.get("https://www.euromaritime.fr/45/2022-exhibitors")
# driver.maximize_window()

driver.find_element(By.ID, 'didomi-notice-agree-button').click()
time.sleep(2)


def main():
    count_1 = []
    company_1 = []
    Company_Website=[]
    check_click = driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[3]/ul[1]/li[*]/a')
    for t in range(2,len(check_click)+2):
        
        company = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[*]/div[1]')
        country = driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[*]/div[2]')
        href = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[*]/div[3]/ul/li/a')
        # print("href====",len(href))
        try:
            u = 0
            for i in company:
                if u == 0:
                    u += 1
                    pass
                else:
                    # print('company======',i.text)
                    company_1.append(i.text)
            # print(company_1)
            p = 0   
            for j in country:
                if p == 0:
                    p += 1
                    pass
                else:
                # print('country =======',j.text)
                    count_1.append(j.text)
            # print(count_1)
                
            for k in href:
                Company_Website.append(k.get_attribute("href"))
            print("compny ==",len(company_1))    
            print("country ==",len(count_1))    
            print("website ==",len(Company_Website))    
    
        except:
            print('None')
            pass

           
        time.sleep(3)
        l = driver.find_element(By.XPATH,f'/html/body/div[2]/div[2]/div[1]/div/div[3]/ul[1]/li[{t}]/a')
        l.click()
        time.sleep(3)
    print('len of company_1 --------- >>> ',len(company_1))
    print('len of count_1 >>>>>>>>> ',len(count_1))
    print('len of Company_Website ==========>>> ',len(Company_Website))
    data = {
        'Business name': company_1,
        'Country': count_1, 
        'Company Website': Company_Website
        }
    print(data,'===============')
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('euromaritime.csv')

main()
driver.close()
