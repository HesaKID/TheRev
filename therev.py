import requests
import sys,re
from bs4 import BeautifulSoup

banner = '''

 /$$$$$$$$ /$$                 /$$$$$$$                      
|__  $$__/| $$                | $$__  $$                     
   | $$   | $$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$  /$$    /$$
   | $$   | $$__  $$ /$$__  $$| $$$$$$$/ /$$__  $$|  $$  /$$/
   | $$   | $$  \ $$| $$$$$$$$| $$__  $$| $$$$$$$$ \  $$/$$/ 
   | $$   | $$  | $$| $$_____/| $$  \ $$| $$_____/  \  $$$/  
   | $$   | $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$   \  $/   
   |__/   |__/  |__/ \_______/|__/  |__/ \_______/    \_/    
                                                             
                                                             
                                                             

 Reverse IP Lookup (viewdns.info)
 Coded By bL@cKID (github.com/RamaCaptainKID)

\n'''
print(banner)

def revip():

    url = sys.argv[1]
    headers = {
    'authority': 'viewdns.info',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    params = (
        ('host', url),
        ('t', '1'),
    )
    req = requests.get('https://viewdns.info/reverseip/', headers=headers, params=params)
    soup = BeautifulSoup(req.text, "html.parser")
    result = soup.findAll("table",{"border":"1"})
    for res in result:
        for td in res.findAll('td'):
            domain = re.findall(r'<td>(.*?)</td>', str(td))
            for dom in domain:
                print(dom)
                open('revip.txt', 'a').write(dom+'\n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage : python ' + sys.argv[0] + ' ip/domain')
    else:
        revip()