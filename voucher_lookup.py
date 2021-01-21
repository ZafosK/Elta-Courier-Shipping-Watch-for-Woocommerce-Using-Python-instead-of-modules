# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:03:46 2021

@author: ZafosK
"""

import re
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

#example domain. You should replace it with yours below
domain='https://cokotech.com' 

url=domain+'/wp-admin'
pages_scraped=30
count=2
driver = webdriver.Chrome()
driver.get(url)
waiting_for_action = input("Type anything, it doesn't matter, as long as you are logged in,\n and then press enter:")
url=domain+'/wp-admin/edit.php?post_status=wc-completed&post_type=shop_order'
with open('vouchers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    while(count<pages_scraped):
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find("table")
        
        
        vouchers=re.findall('ZC\d\d\d\d\d\d\d\d\dGR',tables.text)
        for voucher in vouchers : writer.writerow([voucher])
        url=(domain+'/wp-admin/edit.php?s&post_status=wc-completed&post_type=shop_order&action=-1&m=0&_email_id&_customer_user&paged={}&action2=-1'.format(count))
        count+=1
   

print("DONE!")