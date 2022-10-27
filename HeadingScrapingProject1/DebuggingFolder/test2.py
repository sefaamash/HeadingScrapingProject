from selenium import webdriver
from bs4 import BeautifulSoup
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait

#Array to store Links
links =  ['https://blog.hubspot.com/website/easy-steps-to-speed-up-your-wordpress-site', 'https://www.wpbeginner.com/wordpress-performance-speed/', 'https://www.codeinwp.com/blog/ways-to-speed-up-wordpress/', 'https://kinsta.com/learn/speed-up-wordpress/', 'https://themeisle.com/blog/wordpress-slow/', 'https://www.wpspeedfix.com/speed-up-wordpress-without-plugins/', 'https://blog.hubspot.com/website/best-wordpress-cache-plugins-to-speed-up-a-site', 'https://www.codeinwp.com/blog/ways-to-speed-up-wordpress/', 'https://www.cloudways.com/blog/speed-up-wordpress-site/', 'https://wpengine.com/resources/improve-wordpress-site-speed/', 'https://elementor.com/blog/how-to-speed-up-wordpress-website/', 'https://www.hostinger.com/tutorials/speed-up-wordpress']
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
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




#This Function is scraping Headings h1,h2,h3 from each scraped link from above "Links Function" on HeadingChoice'
def Headings():
    
    #Enter Heading Choices
    #Looping over Each Link to get desired heading tag
  
        driver.get('https://kinsta.com/learn/speed-up-wordpress')
        WebDriverWait(driver,100)
        page = driver.page_source
        soup = BeautifulSoup(str(page), 'html.parser')
        li=['h1','h2','h3']
        h1s=soup.find_all("{}".format(li[0]))
       
        h2s=soup.find_all("{}".format(li[1]))
        
        h3s=soup.find_all("{}".format(li[2]))
        
        for h1 in h1s:
            print("H1"+" "+h1.text)
    
        for h2 in h2s:
                print("H2"+" "+h2.text)

        for h3 in h3s:
               print("H3"+" "+h3.text)
       

Headings()
