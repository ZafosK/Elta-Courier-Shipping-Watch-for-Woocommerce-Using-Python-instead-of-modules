# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:08:40 2021

@author: AdekemetoPtixio
"""


def check_if_delivered(tables):
   for i in tables:
       for j in i:
           for k in j:
              for l in k:
                  for s in l:
                      if s=='ΠΑΡΑΔΟΘΗΚΕ':
                          return(True)
   return False   

def check_if_pending(tables):                
    for i in tables:
       for j in i:
           for k in j:
              for l in k:
                  for s in l:
                      if s=='ΠΡΟΣ ΠΑΡΑΔΟΣΗ' or s=='ΑΡΝΗΣΗ ΠΑΡΑΛΑΒΗΣ' or s=="ΠΑΡΑΛΗΠΤΗΣ ΔΕΝ ΕΝΤΟΠΙΖΕΤΑΙ":
                          return(True)
    return False                 

def check_if_in_transit(tables):
    for i in tables:
       for j in i:
           for k in j:
              for l in k:
                  for s in l:
                      if s=='ΚΛΕΙΣΙΜΟ ΑΠΟ  ΚΕΡΚΥΡΑ - ΠΡΑΚΤΟΡΕΙΟ':
                          return(True)
    return False  

def check_if_voucher_created(tables):
    for i in tables:
       for j in i:
           for k in j:
              for l in k:
                  for s in l:
                      if s=='ΔΗΜΙΟΥΡΓΙΑ ΣΥ.ΔΕ.ΤΑ. ΑΠΟ ΠΕΛΑΤΗ':
                          return(True)
    return False
 
import csv   
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
initURL="https://www.elta-courier.gr/search?br="
with open('voucher_status2.csv','w',newline='') as status_file:
    writer=csv.writer(status_file)
    with open('vouchers.csv', 'r', newline='') as vouchers:
        for voucher in vouchers :
        
            URL=initURL+voucher
            driver.get(URL)
            try:
                sleep(6)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                tables = soup.find_all("table")
                
                if(check_if_delivered(tables)): status='DELIVERED'
                elif(check_if_pending(tables)):status='FOR DELIVERY'
                elif(check_if_in_transit(tables)):status='IN TRANSIT'
                elif(check_if_voucher_created(tables)):status='NOT SCANNED YET'
                else : status='Error'
                
                writer.writerow(([voucher],[status]))
            except :
                writer.writerow(['Error'])
            
print("DONE!")