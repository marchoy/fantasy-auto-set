import time
import getpass
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def start_active_players():
	"""
	Places active players in your lineup for Yahoo! Fantasy Hockey.
	
	username: your Yahoo! username
	password: your Yahoo! password
	days: the number of days you wish to set your lineup
	"""
	driver = webdriver.Chrome()

	driver.implicitly_wait(10)

	driver.get("https://login.yahoo.com/config/login?.src=fantasy&specId=usernameRegWithName&.intl=us&.lang=en-US&.done=https://hockey.fantasysports.yahoo.com/hockey/")

	username_elem = driver.find_element_by_id("login-username")
	username_elem.clear()
	username_elem.send_keys(username)
	username_elem.submit()

	password_elem = driver.find_element_by_id("login-passwd")
	password_elem.clear()
	password_elem.send_keys(password)
	sign_in = driver.find_element_by_id("login-signin")
	sign_in.click()

	my_team = driver.find_element_by_link_text("My Team")
	my_team.click()

	for day in range(days):
		start_players = driver.find_element_by_link_text("Start Active Players")
		start_players.send_keys(Keys.RETURN)

		date = driver.find_element_by_xpath("//span[@class='flyout-title']").text
		print(date)
		
		next_day = driver.find_element_by_xpath("//a[contains(@class, 'Js-next')]")
		next_day.send_keys(Keys.RETURN)

	driver.close()

def days_remaining_in_nhl_season():
	today = date.today()
	last_day_of_nhl_season = date(2018, 4, 9)
	return abs(today - last_day_of_nhl_season).days

username = raw_input("Enter your Yahoo! username: ")
password = getpass.getpass(prompt="Enter your Yahoo! password: ")
days = input("Number of days to set your lineup (" + str(days_remaining_in_nhl_season()) + " days remain): ")

if __name__ == '__main__':
	start_active_players()