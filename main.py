# Coded by METACHAR
# Looking to work with other hit me up on my email @metachar1@gmail.com <--
import sys
import datetime
import selenium
import requests
import time as t
from py_imessage import *
from py_imessage import imessage
from time import sleep
from sys import stdout
from selenium import *
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'


#Config#
parser = OptionParser()
now = datetime.datetime.now()


#Args
#parser.add_option("-u", "--username", dest="username",help="Choose the username")
#parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
#parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the submit button selector")
parser.add_option("--errorsel", dest="errorsel",help= "Choose the message selector")
parser.add_option("--dropdown", dest="dropdown",help= "Choose the dropdown menu's id")
parser.add_option("--phonenumber", dest="phonenumber",help= "Choose the phone number to text")
parser.add_option("--state", dest="state",help= "Choose the state on the website")
#parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()




def wizard():
    print (banner)
    website = raw_input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Enter a website: ')
    sys.stdout.write(color.GREEN + '[!] '+color.CWHITE + 'Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (color.GREEN + '[OK]'+color.CWHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (color.RED + '[!]'+color.CWHITE+ 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print (color.RED + '[X]'+color.CWHITE)
        t.sleep(1)
        print (color.RED + '[!]'+color.CWHITE+ ' Website could not be located make sure to use http / https')
        exit()

    #username_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Username selector: ')
    #password_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Password selector: ')
    login_btn_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    error_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Error message selector: ')
    drop_down =  raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Drop Down Menus ID: ')
    state =  raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the State on the website: ')
    phone_number = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Phone Number to text: ')
    #username = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    #pass_list = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    brutes(login_btn_selector, error_selector, drop_down, website)

def brutes(login_btn_selector, error_selector, drop_down, website):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome()
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(chrome_options=optionss)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                #Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                #Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                # browser.find_element_by_css_selector(password_selector).clear()
                # browser.find_element_by_css_selector(username_selector).clear()
                #Sel_user.send_keys(username)
                sel = Select(driver.find_element_by_id(drop_down))
                time.sleep(0.8)
                #select by select_by_visible_text() method
                sel.select_by_visible_text(state)
                Sel_pas.send_keys(line)
                t.sleep(1)
                error = browser.find_element_by_css_selector(error_selector) #Finds Selector
                print ('------------------------')
                print (color.GREEN + 'Not Available yet')
                print ('------------------------')
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
                phone = phone_number
if not imessage.check_compatibility(phone):
    print ("Not an iPhone")
guid = imessage.send(phone, "The webpage has changed on your computer")
exit()



banner = color.BOLD + color.RED +'''
   ____ _______  __      __     _____ _____ _____ _   _ ______ 
  / __ \__   __| \ \    / /\   / ____/ ____|_   _| \ | |  ____|
 | |  | | | |     \ \  / /  \ | |   | |      | | |  \| | |__   
 | |  | | | |      \ \/ / /\ \| |   | |      | | | . ` |  __|  
 | |__| | | |       \  / ____ \ |___| |____ _| |_| |\  | |____ 
  \____/  |_|        \/_/    \_\_____\_____|_____|_| \_|______|                                  
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by 0vertime
  {8}[{9}-{10}]-->{11}OT VACCINE TOOL                   '''.format(color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN)

driver = webdriver.Chrome()
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1 #count

if options.loginsel == None:
    if options.errorsel == None:
        if options.website == None:
            if options.dropdown == None:
                if options.phonenumber == None:
                    if options.state == None:
                        wizard()


#username = options.username
#username_selector = options.usernamesel
#password_selector = options.passsel
login_btn_selector = options.loginsel
error_selector = options.errorsel
website = options.website
drop_down = options.dropdown
phone_number = options.phonenumber
state = options.state
#pass_list = options.passlist
print (banner)
brutes(login_btn_selector, error_selector, drop_down, website)