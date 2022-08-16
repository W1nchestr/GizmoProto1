from bs4 import BeautifulSoup
import requests
import random
import json

class Yandex:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    host = "yandex.com"
    request = "{\\\"blocks\\\":[{\\\"block\\\":\\\"serp-list_infinite_yes\\\",\\\"params\\\":{\\\"initialPageNum\\\":0},\\\"version\\\":2}]}" #probably dont touch this, otherwise yandex might not respond properly
    expired = False
    
    def __init__(self, yandexuid):
        self.yandexuid = yandexuid
    
    def search(self, text):
        url = f"https://{self.host}/images/search?format=json&request={self.request}&text={text}&ncrnd=0.0599365020021096"
        
        headers = {
            "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Cookie": f"mda=0; yandexuid={self.yandexuid}; yuidss={self.yandexuid}; is_gdpr=0; yp=1639553678.ygu.1#1953187021.sp.family%3A2#1636963239.zlgn_nzdlb.1#1637566977.szm.1%3A1920x1080%3A1920x880#1637048576.nps.5857137911%3Aclose#1668498819.ln_tp.01",
            "Host": self.host,
            "TE": "trailers",
            "Referer": "https://yandex.com/images/search?text=" + text,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": self.user_agent,
            "X-Requested-With": "XMLHttpRequest"
        }
        
        if self.expired or self.yandexuid == None:
            print("Fatal: yandexuid expired!") #if your yandexuid is expired you will need to open a browser, clear browsing data for yandex, and grab the new yandexuid from the request cookies
            raise Exception("YandexuidExpired")
        
        req = requests.get(url=url, headers=headers, timeout=5)
        
        if req.json().get("type") == "captcha": #detect if yandex is sending a captcha instead of normal results - if so; rip.
            self.expired = True
            raise Exception("YandexuidExpired")
        
        html = req.json()['blocks'][0]['html']
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.findAll("div", {"data-bem" : True}) #find all div elements that have the "data-bem" attrribute
        
        results = [] 
        
        for elem in data:
            try:
                result = json.loads(elem['data-bem'].replace("\\\"", "\"")) #grabbing json data which is stored in an html-element attribute (weirdbutok)
                if result.get("serp-item"): #image related data is only present in serp-item, so ignore all other data
                    results.append(result) 
            except:
                pass
        
        images = []
        
        for part in results:
            if part["serp-item"].get("preview"):
                url = part["serp-item"]["preview"][0]["url"] #grab image url
                
                if "?" in url:
                    url = url.split('?')[0] #remove all query parameters, not essential but may fix some issues.
                
                if url not in images:
                    images.append(url) #append the image to the final images list, if not already present.
        
        return images #returns list of image urls (or empty list if no results)