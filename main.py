from os import getcwd
from rich.console import Console
import pyautogui
from helium import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
#from mainfunctions import Funcs
def f(driv, id):
	return WebDriverWait(driv, 9).until(EC.presence_of_element_located((By.ID, id)))
def fe(driv, id):
	return WebDriverWait(driv, 99999).until(EC.presence_of_element_located((By.ID, id))) #myresult-indicator
def c(driv, class_name):
	return WebDriverWait(driv, 9).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
def ce(driv, class_name):
	return WebDriverWait(driv, 1).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
def t(driv, t1):
	return WebDriverWait(driv, 9).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, t1)))
def n(driv, t2):
	return WebDriverWait(driv, 9).until(EC.presence_of_element_located((By.NAME, t2)))
def x(driv, t3):
	return WebDriverWait(driv, 9).until(EC.presence_of_element_located((By.XPATH, t3)))

Config.implicit_wait_secs = 9
console = Console(style="purple on black")
console.set_window_title("ATI Completer")

def highlight(element, effect_time, color, border):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

def newInstance():
	firstrun = True
	question = ""
	answered = False
	global answer
	global answers
	global prevq
	with console.screen(style="bold white on red") as screen:
		console.rule("[bold white] Working...")
		while True:
			try:
				if firstrun==True:
					with console.status("Running a new instance for first time..."):
						options = webdriver.ChromeOptions()
						options.add_experimental_option('excludeSwitches', ['enable-logging'])
						driver = webdriver.Chrome(options=options, executable_path='C:/chromedriver.exe')
						driver2 = webdriver.Chrome(options=options, executable_path='C:/Users/chromedriver.exe')
						driver.get("https://www.atitesting.com/login")
						driver2.get("https://quizlet.com/login")

					# input("found sign in")
						f(driver,"username").send_keys("rjwilder1")
						f(driver,"password").send_keys("Cark2001$")
						f(driver,"password").send_keys(Keys.ENTER)
						console.print("Logged in ATI")

						f(driver2,"username").send_keys("legacywrld")
						f(driver2,"password").send_keys("Cark2001$")
						f(driver2,"password").send_keys(Keys.ENTER)
						firstrun = False
						console.print("Logged in Quizlet")
					with console.status("Please navigate to ATI Quiz..."):
						driver.switch_to.frame(fe(driver, "assessmentFrame"))
							#driver.switch_to.frame(driver.find_element_by_id("assessmentFrame"))
							#assessmentFrame
							#driver.execute_script("var iframes = document.querySelectorAll('iframe'); for (var i = 0; i < iframes.length; i++) { iframes[i].parentNode.removeChild(iframes[i]); }")
						console.print("ATI iFrame disabled - Script executed")
				if question != f(driver, "highlightWordsText").text:
					console.rule("[bold white] Searching for answer...")
					#Begin with ATI
					question = f(driver, "highlightWordsText").text
					middle = len(question) // 2
					pyperclip.copy(question[middle-6:middle+6])
					console.print("Question: " + question)
						#Begin with Quizlet
					driver2.get("https://google.com")
					n(driver2, "q").send_keys(question + " quizlet")
					n(driver2, "q").send_keys(Keys.ENTER)
					t(driver2, "quizlet").click()
					time.sleep(1)
					driver2.execute_script("window.scrollTo(0, document.body.scrollHeight);")
					console.rule("[bold white] Found answer! Paste into browser...")
					#while answered == False:
					#	try:
					#		ce(driver2, "myresult-indicator")
					#		answered = True
					#	except:
					#		pass

					#console.log("Answered!")
					time.sleep(1)
					#f(driver2, "moveNext").click()
					#myresult-indicator
						#pyautogui.hotkey('ctrl','f') 
						#pyautogui.typewrite(question[:25])    
						#pyautogui.hotkey('Return')
			except Exception as ex:
				console.print(ex)

newInstance()
