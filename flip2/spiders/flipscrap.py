import scrapy
#import the item container class from items.py
from ..items import Flip2Item



class FlipscrapSpider(scrapy.Spider):
    name = 'flipscrap'
    allowed_domains = ['https://www.flipkart.in/']

    #mentioning the flipkart site and setting page numbers from 1 to 10 since one page conisists
    #og about 24 results

    start_urls = [
        'https://www.flipkart.com/apple-iphone-13-pro-max-sierra-blue-1-tb/p/itm9b0652604b403?pid=MOBG6VF5YHYZNNMM&lid=LSTMOBG6VF5YHYZNNMMQQFXLX&marketplace=FLIPKART&q=iphone+13+pro+max&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_6_4_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_6_4_na_na_ps&fm=SEARCH&iid=c19ff05e-018d-47e7-a341-f31c280987d8.MOBG6VF5YHYZNNMM.SEARCH&ppt=sp&ppn=sp&ssid=c611px39o00000001634627663059&qH=5556902974bb931a'
        ]
    def parse(self, response):


        items = Flip2Item()

        #extracting name, price and specs of mobiles

        name=response.xpath('//div/h1[@class = "yhB1nd"]/span[@class = "B_NuCI"]/text()').extract()
        price=response.xpath('//div[@class = "_30jeq3 _16Jk6d"]/text()').extract()
        #specs are listed as li elements
        memory=response.xpath('//div[@class = "_2418kt"]/ul/li[1]/text()').extract()
        camera=response.xpath('//div[@class = "_2418kt"]/ul/li[3]/text()').extract()
        display=response.xpath('//div[@class = "_2418kt"]/ul/li[2]/text()').extract()
        cpu=response.xpath('//div[@class = "_2418kt"]/ul/li[4]/text()').extract()
        
        
        items['name'] = name
        items['price'] = price
        items['memory'] = memory
        items['camera'] = camera
        items['display'] = display
        items['cpu'] = cpu


        #for Mobile_Name, Mobile_Price, Mobile_Memory, Mobile_Camera, Mobile_Battery, Mobile_CPU in zip(name, price, memory,camera,battery,cpu):
           # yield {'Mobile_Name': Mobile_Name.strip(), 'Mobile_Price': Mobile_Price.strip(), 'Mobile_Memory': Mobile_Memory.strip(), 'Mobile_Camera': Mobile_Camera.strip(),'Mobile_Battery': Mobile_Battery.strip(),'Mobile_CPU': Mobile_CPU.strip()}
       # pass
        
        yield items

        