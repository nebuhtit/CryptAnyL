# -*- coding: utf8 -*-


import re
import time
import selenium
import sys
from sys import exc_info
from traceback import extract_tb

from selenium import webdriver

#from selenium.webdriver.common.keys import Keys




# from selenium.webdriver.chrome.options import Options
# opts = Options()
# opts.add_argument("user-agent=")

def forma(a,b):
    # Write vars
    l = str(a+"@@@@"+b)
    print(l)
forma("gek","meg")

def out_forma(str):
    # Read vars
    l = str.split('@@@@')
    a = l[0]
    b = l[1]
    return a, b
a, b = out_forma("bulbobek@@@@romanovich")
print(a, b)




def WRITE(text):
    # Write text in common sheet
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    PATH = '/Users//Downloads/chromedriver'  # PATH TO YOUR CHROME WEB DRIVER
    dr = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_opt)
    link = ("https://WRITE_HERE_LINK_FOR_YOUR_G_SHEET")
    #dr.set_window_size(767, 1235)
    #dr.set_window_position(1300,0)
    dr.get(link)
    time.sleep(0)
    el = dr.find_element_by_xpath('//*[@id="t-formula-bar-input"]/div')
    #print(el.get_attribute('outerHTML'))
    el.click()
    el.clear()
    el.send_keys(text)
    print(el.text)
    save_changes = dr.find_element_by_xpath('//*[@id="docs-file-menu"]')
    time.sleep(2)
    save_changes.click()
    time.sleep(2)
    dr.close()
WRITE('hello')

def READ():
    # Read text from common sheet
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    PATH = '/Users//Downloads/chromedriver' # PATH TO YOUR CHROME WEB DRIVER
    dr = webdriver.Chrome(executable_path=PATH,chrome_options=chrome_opt)
    link = ("https://WRITE_HERE_LINK_FOR_YOUR_G_SHEET")
    #dr.set_window_size(767, 1235)
    #dr.set_window_position(1300,0)
    dr.get(link)
    time.sleep(0)
    el = dr.find_element_by_xpath('//*[@id="t-formula-bar-input"]/div')
    #print(el.get_attribute('outerHTML'))
    el.click()
    #el.clear()
    #el.send_keys(text)
    readed_text = el.text
    print(el.text)
    save_changes = dr.find_element_by_xpath('//*[@id="docs-file-menu"]')
    time.sleep(2)
    save_changes.click()
    time.sleep(2)
    dr.close()
    return readed_text
t = READ()
print(t)
