
import requests
from bs4 import BeautifulSoup

USER_AGENT = ["Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
"Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0b7pre) Gecko/20100921 Firefox/4.0b7pre",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mediapartners-Google",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)",
"Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)",
"Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)",
"Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
"Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
"Sosospider+(+http://help.soso.com/webspider.htm)",
"msnbot/2.0b (+http://search.msn.com/msnbot.htm)",
"Wotbox/2.01 (+http://www.wotbox.com/bot/)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"]

url = "https://www.esiee.fr/"

response = requests.get(url)
soup = BeautifulSoup(response.text)


class http_requester:
    def __init__(self,userAgent,timeOut = 10):
        self.userAgent = userAgent
        self.timeOut = timeOut

    def try_request(self,url,retry=0):
        if(retry < 4):
            try:
                headers = {"UserAgent":str(self.userAgent)}
                response = requests.get(url,headers=headers,timeout=self.timeOut)
                print(response.content[0:1000])
            except requests.exceptions.Timeout:
                print("Retrying...")
                self.try_request(url,retry + 1)
        else:
            print("TimeOut: too many retries.")
            
    def delete_space(self,chain):
        new_chain = chain.replace(" ","")
        return new_chain

    def clean_string(self,chain):
        new_chain = ''.join(filter((str.isalnum or str(" ")), chain))
        return new_chain

    def get_soup(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        return soup

http_Obj = http_requester("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",5)

word = "Hello! How are u."
new_word = http_Obj.delete_space(word)
new_word_2 = http_Obj.clean_string(word)

print(new_word)
print(new_word_2)


# http_Obj.try_request("https://www.google.com:81/",0)