#!/usr/python3 

from termcolor import colored
import webbrowser
import subprocess
import time

subprocess.run (["clear"])

print ("Welcome to Dorky")
print ("A Google dorking script")
print ()
print ("Yes the script's name is stupid. I'm unoriginal.")
print ()

def MainMenu():
	print ("+Main Menu+")
	print ("1> Find cached websites")
	print ("2> Find FTP servers")
	print ("3> Alt search for FTP servers")
	print ("4> Find webcams")
	print ("5> Find database passwords")
	print ("6> Other Dorks")
	print ("7> Find logs")
	print ("8> Credits")	

	#input
	selection=int(input("Choose 1-8: "))

	#cached search
	if selection==1:
		cached()
	
	#ftp search
	if selection==2:
		ftp()
	
	#alt ftp search
	if selection==3:
		altftp()
	
	#webcam search
	if selection==4:
		webcam()
		
	#database search
	if selection==5:
		database()

	#other dorks menu		
	if selection==6:
		other()

	#log search
	if selection==7:
		logs()

	#credits
	if selection==8:
		credits()	

	#invalid character
	else:
		print ("Invalid character")
		subprocess.run (["clear"])
		MainMenu()

#find cached sites
def cached():
	oldsite=input ("Site to find old version of: ")
	print(oldsite)
	webbrowser.open ("www.google.com/search?q=cache: " + oldsite, new=1)
	subprocess.run (["clear"])

#no need to call main menu function after option function

#ftp search
def ftp():
	webbrowser.open ("www.google.com/search?q=inurl:/proc/self/cwd", new=1)
	print ("Searching for FTP servers...")
	time.sleep (1)
	subprocess.run (["clear"])

#alt ftp search
def altftp():
	webbrowser.open ("""www.google.com/search?q=intitle:"index of" inurl:ftp""", new=1)
	print ("Searching for FTP servers...")
	time.sleep (1)
	subprocess.run (["clear"])

#webcam search
def webcam():
	webbrowser.open ("""www.google.com/search?q=intitle:"webcamXP 5" """)
	print ("Searching for webcams...")
	time.sleep (1)
	subprocess.run (["clear"])
	
#database search 
def database():
	webbrowser.open ("www.google.com/search?q=db_password filetype:env", new=1)
	print ("Searching for database passwords...")
	time.sleep (1)
	subprocess.run (["clear"])

#credits
def credits():
	subprocess.run (["clear"])
	print ("+The Credits+")
	print ("Inspired by Null Byte's Google Dorks video")
	print ("video link: https://www.youtube.com/watch?v=u_gOnwWEXiA&t=136s")
	print ()
	print ("Coded by Xt3ns1s in python 3.8.2")
	print ()
	print ("June 2020")
	time.sleep (3)
	subprocess.run (["clear"])
	MainMenu()

#other dorks
def other():
	subprocess.run (["clear"])
	print ("Other Dorks")
	print ("1> Find Git Sites")
	print ("2> Find PHP variables")
	print ("3> Find Apache server configs")
	print ("4> Find Nesssus vuln reports")
	print ("5> Back to Main Menu")
	selection=int(input("Choose 1-5: "))
	
	#git search
	if selection==1:
		git()
	
	#php search
	if selection==2:
		php()

	#apache search
	if selection==3:
		apache()

	#nessus search
	if selection==4:
		nessus()
	
	else:
		subprocess.run (["clear"])
		print ("Invalid character!")
		time.sleep (1)
		other()

#git site search
def git():
	webbrowser.open ("www.google.com/search?q=filetype:inc php -site:github.com -site:sourceforge.net", new=1)
	print ("Searching for Git sites...")
	time.sleep (1)
	subprocess.run (["clear"])

#php search
def php():
	webbrowser.open ("""www.google.com/search?q=filetype:php "Notice: Undefined variable: data in" -forum""")
	print ("Searching for PHP variables...")
	time.sleep (1)
	subprocess.run (["clear"])

#apache search
def apache():
	webbrowser.open ("""www.google.com/search?q=intitle:"WAMPSERVER homepage""Server Configuration""Apache Version" """)
	print ("Searching for apache configs...")
	time.sleep (1)
	subprocess.run (["clear"])

#nessus report search
def nessus():
	webbrowser.open ("""www.google.com/search?q=intitle:"report" ("qualys"|"acunetix"|"nessus"|"netsparker"|"nmap") filetype:pdf""")
	print ("Searching for nessus reports...")
	time.sleep (1)
	subprocess.run (["clear"])

#logs menu
def logs():
	subprocess.run (["clear"])
	print ("+Logs Menu+")	
	print ("1> Username Logs")
	print ("2> Password Logs")
	print ("3> Admin Logs")
	print ("4> Root logs")
	print ("5> IP Logs")	
	print ("6> Port Logs")
	print ("7> Rom-0 Logs")
	print ("8> Custom allintext")
	print ("9> Back to Main Menu")
	#print ("10> Kill open brower windows")

	
	#user input for main menu

	selection=int(input("Choose 1-9: "))

	#username log search
	
	if selection==1:
		username()	
	
	#password logs
	
	if selection==2:
		password()	

	#admin logs

	if selection==3:
		admin()
		
	#root logs

	if selection==4:
		root()

	#ip logs
	
	if selection==5:
		ip()

	#port logs
	
	if selection==6:
		port()
	
	#rom-0 logs

	if selection==7:
		rom()

	#custom allintext
	
	if selection==8:
		custom()	

	#Back to Main Menu
	
	if selection==9:
		mainmenu()

	#invalid character
	else:
		print ("Invalid character")
		subprocess.run (["clear"])
		time.sleep (1)	
		logs()

#username log search 

def username():

	webbrowser.open ("www.google.com/search?q=allintext:username filetype:log", new=1)
	time.sleep (1)
	print ("Searching for usernames...")

#password log search

def password():

	webbrowser.open ("www.google.com/search?q=allintext:password filetype:log", new=1)
	time.sleep (1)
	print ("Searching for passwords...")

#admin log search

def admin():

	webbrowser.open ("www.google.com/search?q=allintext:admin filetype:log", new=1)
	time.sleep (1)
	print ("Searching for admin logs...")

#root log search

def root():

	webbrowser.open ("www.google.com/search?q=allintext:root filetype:log", new=1)
	time.sleep (1)
	print ("Searching for root logs...")

#ip log search

def ip():

	webbrowser.open ("www.google.com/search?q=allintext:ip filetype:log", new=1)
	time.sleep (1)
	print ("Searching for ips...")

#port logs

def port():
	webbrowser.open (" www.google.com/search?q=allintext:port filetype:log", new=1)
	time.sleep (1)
	print ("Searching for port logs...")	

#rom-0 logs search

def rom():

	webbrowser.open ("www.google.com/search?q=allintext:rom-0 filetype:log", new=1)
	time.sleep (1)
	print ("Searching for rom-0 logs...")

#custom allintext search

def custom():

	custom=input ("Custom allintext search: ")
	time.sleep (1)
	webbrowser.open ("www.google.com/search?q=allintext:{0} filetype:log".format(custom),new=1)

#calls main menu

def mainmenu():
	
	subprocess.run(["clear"])
	MainMenu()
	
MainMenu()
