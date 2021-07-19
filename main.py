#2021 Attempt

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import docx2txt


resume = docx2txt.process('test.docx')
print(resume)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter: ')
url = 'https://jobs.hess.com/job/Houston-Drilling-Engineer-Job-TX-77001/752777500/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#tags = soup('meta')
#print(tags)
#print(soup)