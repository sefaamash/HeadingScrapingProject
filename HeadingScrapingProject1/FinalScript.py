from selenium import webdriver
from bs4 import BeautifulSoup
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait

#Array to store Links
links = []

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
#False will open browser True will not open script on browser
options.headless = False
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--log-level=3')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='dirhect://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--disable-3d-apis")
options.add_argument("--disable-browser-side-navigation")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

#This function is scraping links from google
def Links(searchQuery):
    driver.get('https://www.google.com/search?q='+searchQuery)
    WebDriverWait(driver,100)
    page = driver.page_source
    soup = BeautifulSoup(str(page), 'html.parser')
    linksContainer = soup.find_all("div", {'class': 'yuRUbf'})
    for link in linksContainer:
        linkResult = link.a['href']
        links.append(linkResult)
   


#This Function is scraping Headings h1,h2,h3 from each scraped link from above "Links Function" on HeadingChoice'
def Headings():
    #Enter Search Query 
    searchQuery = input("Enter Something to search:")
    print("Googling.............................")
    
    #Execution Of Links Function
    Links(searchQuery)
    
    #Enter Heading Choice 
    headingChoice = input("Enter from h1 h2 h3 with , in between heading choices: ")
   
    #Making TextFile
    f = open("TextFiles/{}.txt".format(searchQuery), "w",encoding="utf-8")
    
    #HeadingConditions
    if (headingChoice == "h1" or headingChoice == "h2" or headingChoice == "h3"):
        f.write("......................{}'S ............................h1".format(headingChoice.upper()))
    elif (headingChoice == "h1,h2" or headingChoice == "h2,h1" or headingChoice == 'h1,h3' or headingChoice == 'h3,h1' or headingChoice == 'h2,h3' or headingChoice == 'h3,h2'):
        f.write("......................{}'S AND {}'S ............................".format(
            headingChoice.split(',')[0].upper(), headingChoice.split(',')[1].upper()))
    elif (headingChoice == 'h1,h2,h3' or headingChoice == 'h1,h3,h2' or headingChoice == 'h2,h1,h3 ' or headingChoice == 'h2,h3,h1' or headingChoice == 'h3,h1,h2' or headingChoice == 'h3,h2,h1'):
        f.write("......................{}'S {}'S {}'S ............................".format(headingChoice.split(
            ',')[0].upper(), headingChoice.split(',')[1].upper(), headingChoice.split(',')[2].upper()))
    
    #Looping over each link and scrapping desired heading tag
    for i in range(len(links)):
        driver.get('{}'.format(links[i]))
        WebDriverWait(driver,30)
        page = driver.page_source
        soup = BeautifulSoup(str(page), 'html.parser')
        
        #Single Heading Choice Condition
        if (headingChoice == "h1" or headingChoice == "h2" or headingChoice == "h3"):
            response = soup.find_all(headingChoice)
            for headings in response:
                hText = headings.text
                f.write("\n"+hText)
            f.write("\n------------------------{} Ends-----------------------".format(links[i]))
        #Double Heading Choice Condition
        elif (headingChoice == "h1,h2" or headingChoice == "h2,h1" or headingChoice == 'h1,h3' or headingChoice == 'h3,h1' or headingChoice == 'h2,h3' or headingChoice == 'h3,h2'):
            response1 = soup.find_all(headingChoice.split(',')[0])
            response2 = soup.find_all(headingChoice.split(',')[1])
            for headings1 in response1:
                hr1Text = headings1.text
                f.write('\n'+hr1Text)
            for heading2 in response2:
                hr2Text = heading2.text
                f.write("\n"+hr2Text)
            f.write("\n------------------------{} Ends-----------------------".format(links[i]))
        #Triple Heading Choice Condition
        elif (headingChoice == 'h1,h2,h3' or headingChoice == 'h1,h3,h2' or headingChoice == 'h2,h1,h3 ' or headingChoice == 'h2,h3,h1' or headingChoice == 'h3,h1,h2' or headingChoice == 'h3,h2,h1'):
            response1 = soup.find_all(headingChoice.split(',')[0])
            response2 = soup.find_all(headingChoice.split(',')[1])
            response3 = soup.find_all(headingChoice.split(',')[2])
            for headings1 in response1:
                hr1Text = headings1.text
                f.write('\n'+hr1Text)
            for heading2 in response2:
                hr2Text = heading2.text
                f.write("\n"+hr2Text)
            for heading3 in response3:
                hr3Text = heading3.text
                f.write("\n"+hr3Text)
            f.write("\n------------------------{} Ends-----------------------".format(links[i]))
        else:
            print("Heading Tag Not Valid and put , in between headings input  ")
            print("Select from \n h1 \n h2 \n h3")
            break
        


Headings()
driver.close()