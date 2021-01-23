# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:03:46 2021

@author: https://github.com/ZafosK/
"""

import re   
from selenium import webdriver
from bs4 import BeautifulSoup
import csv    #Since we will be noting our vouchers on a csv

#example domain. You should replace it with yours below
domain='https://cokotech.com' 

url=domain+'/wp-admin' #You will also have to change this if your wp-admin, is not your login page
pages_scraped=30       #The final number of page you wish to scrape for vouchers
count=2  #the number of the second page scraped beginning 
driver = webdriver.Chrome()  #This runs the automated Chromium webdriver. Needs to be added to PATH
driver.get(url)
waiting_for_action = input("Type anything, it doesn't matter, as long as you are logged in,\n and then press enter:") #After you log in to your wordpress dashboard, press enter next to the message in the console
url=domain+'/wp-admin/edit.php?post_status=wc-completed&post_type=shop_order'  #this redirects the webdriver to the completed orders page so that we can start scraping
with open('vouchers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    while(count<pages_scraped):
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find("table")
        
        
        vouchers=re.findall('ZC\d\d\d\d\d\d\d\d\dGR',tables.text) #The regex used to find the vouchers on our webpage. You will have to edit this if your vouchers look different
        for voucher in vouchers : writer.writerow([voucher]) #printing the voucher number on a csv
        url=(domain+'/wp-admin/edit.php?s&post_status=wc-completed&post_type=shop_order&action=-1&m=0&_email_id&_customer_user&paged={}&action2=-1'.format(count))
        count+=1
   

print("DONE!")
