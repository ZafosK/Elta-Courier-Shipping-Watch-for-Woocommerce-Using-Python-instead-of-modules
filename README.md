# Shipping-Watch-for-Woocommerce-Using-Python-instead-of-modules

## Quick Summary

A not so simple way for woocommerce users to extract their websites orders' vouchers, without using SQL or having database access. 
These 2 scripts are useless for most people considering the fact that ELTA courier offers software that does the same job, and of course is 
way easier to set up and running

## What the code does

This repository consists of two scipts, meant not to be used simultaneously, both using selenium and BeautifulSoup to scrape the necessary information.
The first one, collects all the vouchers from the specified pages. The second one, scrapes information from ELTA Couriers' page using the list created from the first script
in order to create a new list, including the status of each order.

## Requirements

### For voucher_lookup.py

1. chromium webdriver

2. Python with the following modules installed on your environment
   
