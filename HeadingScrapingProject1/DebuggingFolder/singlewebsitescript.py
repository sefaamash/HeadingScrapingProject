from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--log-level=3")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.mygreatlearning.com/blog/top-highest-paying-jobs-in-the-world/")
page=driver.page_source
soup=BeautifulSoup(str(page),'html.parser')
bodyTag=soup.body.main
#print(bodyTag.prettify())

if (bodyTag):

	h3s=bodyTag.find_all('h3')
	h2s=bodyTag.find_all('h2')
	h1s=bodyTag.find_all('h1')

	for h3 in h3s:
		print(h3.text)
	print("-----------------------------")
	for h2 in h2s:
		print(h2.text)
	print("-----------------------------")
	for h1 in h1s:
		print(h1.text)
	print("-----------------------------")
