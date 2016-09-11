from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from getpass import getpass
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
display = Display(visible=0,size=(800,600))
display.start()
driver = webdriver.Firefox()
try:
	driver.get("https://172.16.8.45")
	print 'Connection successful'
except:
	print 'No internet Connection'
	driver.quit()
username = raw_input('Enter Username: ')
password = getpass('Enter password: ')
uname = driver.find_element_by_name("username")
uname.send_keys(username)
pword = driver.find_element_by_name("password")
pword.send_keys(password)
submitb = driver.find_element_by_id("submit")
submitb.click()
#time.sleep(5)
att = "https://172.16.8.45/index.php/attendance/student_attendance"
htmlunit=driver.find_element_by_tag_name('html')
curWindowHndl = driver.current_window_handle
htmlunit.send_keys(Keys.CONTROL + 't'+Keys.CONTROL,att) 
htmlunit.send_keys(Keys.ENTER)
#time.sleep(5)
driver.switch_to_window(curWindowHndl)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "session_year_attendance")))
session_year = driver.find_element_by_id("session_year_attendance")
year = session_year.find_elements_by_tag_name("option")
year[2].click()
session = driver.find_element_by_id("session_attendance")
season = session.find_elements_by_tag_name("option")
season[1].click()
sem = driver.find_element_by_id("semester_attendance")
sem_att = sem.find_elements_by_tag_name("option")
sem_att[1].click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"submit")))
submitb_att = driver.find_element_by_id("submit")
submitb_att.click()
#time.sleep(2)
for i in xrange(2,8):
	sub = "/html/body/div[2]/aside[2]/section[2]/div[3]/div/table[1]/tbody/tr["+str(i)+"]/td[3]"
	WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,sub)))
	el = driver.find_element_by_xpath(sub)
	print el.text,
	print "  -  ",
	percent = "/html/body/div[2]/aside[2]/section[2]/div[3]/div/table[1]/tbody/tr["+str(i)+"]/td[7]/center"
	WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,percent)))
	el1 = driver.find_element_by_xpath(percent)
	tex = el1.text
	if tex=="class not started":
		print "Not uploaded"
	else:
		print tex
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w') 
driver.switch_to_window(curWindowHndl)
display.stop()
driver.quit()