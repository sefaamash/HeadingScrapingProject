from selenium import webdriver
from bs4 import BeautifulSoup
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
import csv
import pandas as pd

h1 = []
h2 = []
h3 = []
# Array to store Links
links = []
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument(f'user-agent={user_agent}')
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


# This function is scraping links from google
def Links(searchQuery):
    driver.get('https://www.google.com/search?q='+searchQuery)
    page = driver.page_source
    soup = BeautifulSoup(str(page), 'html.parser')
    linksContainer = soup.find_all("div", {'class': 'yuRUbf'})
    for link in linksContainer:
        linkResult = link.a['href']
        links.append(linkResult)
    print("Query result Links", links)

# This Function is scraping Headings h1,h2,h3 from each scraped link from above "Links Function" on HeadingChoice'


def Headings():
    # Enter Search Query
    searchQuery = input("Enter Something to search:")
    print("Googling.............................")

    # Links Function
    Links(searchQuery)

    # Enter Heading Choices
    headingChoice = input(
        "Enter from h1 h2 h3 with , in between heading choices: ")

    # Heading-Conditions
    if (headingChoice == "h1" or headingChoice == "h2" or headingChoice == "h3"):

        print("......................{}'S ............................h1".format(
            headingChoice.upper()))

    elif (headingChoice == "h1,h2" or headingChoice == "h2,h1" or headingChoice == 'h1,h3' or headingChoice == 'h3,h1' or headingChoice == 'h2,h3' or headingChoice == 'h3,h2'):

        print("......................{}'S AND {}'S ............................".format(
            headingChoice.split(',')[0].upper(), headingChoice.split(',')[1].upper()))

    elif (headingChoice == 'h1,h2,h3' or headingChoice == 'h1,h3,h2' or headingChoice == 'h2,h1,h3 ' or headingChoice == 'h2,h3,h1' or headingChoice == 'h3,h1,h2' or headingChoice == 'h3,h2,h1'):
        print("......................{}'S {}'S {}'S ............................".format(headingChoice.split(
            ',')[0].upper(), headingChoice.split(',')[1].upper(), headingChoice.split(',')[2].upper()))

    # Looping over Each Link to get desired heading tag
    for i in range(len(links)):
        driver.get('{}'.format(links[i]))
        WebDriverWait(driver, 100)
        page = driver.page_source
        soup = BeautifulSoup(str(page), 'html.parser')
        main = soup.body.main
        body = soup.body
        if (main):

            # Single Heading Choices
            if (headingChoice == "h1" or headingChoice == "h2" or headingChoice == "h3"):

                response = main.find_all(headingChoice)
                for headings in response:
                    hr1Text = headings.text
                    print(hr1Text)
                    h1.append(hr1Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))

            # Double Heading Choices
            elif (headingChoice == "h1,h2" or headingChoice == "h2,h1" or headingChoice == "h1,h3" or headingChoice == "h3,h1" or headingChoice == "h2,h3" or headingChoice == "h3,h2"):
                response1 = main.find_all(headingChoice.split(',')[0])
                response2 = main.find_all(headingChoice.split(',')[1])
                for headings1 in response1:
                    hr1Text = headings1.text
                    print(hr1Text)
                    h1.append(hr1Text)

                for heading2 in response2:
                    hr2Text = heading2.text
                    print(hr2Text)
                    h2.append(hr2Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))

            # Triple Heading Choices
            elif (headingChoice == "h1,h2,h3" or headingChoice == "h1,h3,h2" or headingChoice == "h2,h1,h3" or headingChoice == "h2,h3,h1" or headingChoice == "h3,h1,h2" or headingChoice == "h3,h2,h1"):
                response1 = main.find_all(headingChoice.split(',')[0])
                response2 = main.find_all(headingChoice.split(',')[1])
                response3 = main.find_all(headingChoice.split(',')[2])
                for headings1 in response1:

                    hr1Text = headings1.text
                    print(hr1Text)
                    h1.append(hr1Text)

                for heading2 in response2:

                    hr2Text = heading2.text
                    print(hr2Text)
                    h2.append(hr2Text)

                for heading3 in response3:

                    hr3Text = heading3.text
                    print(hr3Text)
                    h3.append(hr3Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))
            else:
                print("Heading Tag Not Valid and put , in between headings input  ")
                print("Select from \n h1 \n h2 \n h3")
                break
        elif (body):
            # Single Heading Choices
            if (headingChoice == "h1" or headingChoice == "h2" or headingChoice == "h3"):

                response = body.find_all(headingChoice)
                for headings in response:
                    hr1Text = headings.text
                    print(hr1Text)
                    h1.append(hr1Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))

            # Double Heading Choices
            elif (headingChoice == "h1,h2" or headingChoice == "h2,h1" or headingChoice == "h1,h3" or headingChoice == "h3,h1" or headingChoice == "h2,h3" or headingChoice == "h3,h2"):
                response1 = body.find_all(headingChoice.split(',')[0])
                response2 = body.find_all(headingChoice.split(',')[1])
                for headings1 in response1:
                    hr1Text = headings1.text
                    print(hr1Text)
                    h1.append(hr1Text)

                for heading2 in response2:
                    hr2Text = heading2.text
                    print(hr2Text)
                    h2.append(hr2Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))

            # Triple Heading Choices
            elif (headingChoice == "h1,h2,h3" or headingChoice == "h1,h3,h2" or headingChoice == "h2,h1,h3" or headingChoice == "h2,h3,h1" or headingChoice == "h3,h1,h2" or headingChoice == "h3,h2,h1"):
                response1 = body.find_all(headingChoice.split(',')[0])
                response2 = body.find_all(headingChoice.split(',')[1])
                response3 = body.find_all(headingChoice.split(',')[2])
                for headings1 in response1:

                    hr1Text = headings1.text
                    print(hr1Text)
                    h1.append(hr1Text)
                for heading2 in response2:

                    hr2Text = heading2.text
                    print(hr2Text)
                    h2.append(hr2Text)

                for heading3 in response3:

                    hr3Text = heading3.text
                    print(hr3Text)
                    h3.append(hr3Text)

                print(
                    "------------------------{} Ends-----------------------".format(links[i]))
            else:
                print("Heading Tag Not Valid and put , in between headings input  ")
                print("Select from \n h1 \n h2 \n h3")
                break

    df1 = pd.DataFrame({"H1": h1})
    df2 = pd.DataFrame({"H2": h2})
    df3 = pd.DataFrame({"H3": h3})
    pd.concat([df1, df2, df3], axis=1).to_csv(
        "HeadingScrapingProject2/CsvFiles/{}.csv".format(searchQuery), index=False)


Headings()
driver.close()
