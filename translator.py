import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument('--headless')

s=FirefoxService(GeckoDriverManager().install())
d = webdriver.Firefox(service=s, options=options)


para=input('Enter:')
handle=open(para)


x=''
for line in handle:
    if line!='\n':
        if '/' in line:
            line=line.replace('/',r"\/")
        list=line.split(' ')
        if '-' and '\n' in list[-1]:
            list[-1]=list[-1].replace('-','')
            list[-1]=list[-1].replace('\n','')
            x+=' '.join(list)
    else:
        text=str(x)
        d.get("https://www.deepl.com/translator#en/de/"+text)
        time.sleep(3)

        output = 'target-dummydiv'
        id = d.find_element(By.ID, output)
        print(id.get_attribute('innerHTML'))
        outputfile = open('output.txt', 'a')
        print(id.get_attribute('innerHTML'), file = outputfile)
        print(file=outputfile)
        outputfile.close()
        x=''





