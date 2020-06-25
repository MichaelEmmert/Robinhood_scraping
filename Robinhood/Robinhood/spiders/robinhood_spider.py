from Robinhood.items import RobinhoodItems
from scrapy import Spider, Request
import pandas as pd

class RobinhoodSpider(Spider):
    name = 'robinhood_spider'
    allower_urls = ['https://www.Robinhood.com']
    start_urls = ['https://robinhood.com/stocks/KO']

    def parse(self, response):
        tickers = pd.read_csv('C:/Users/Micha/Desktop/JupyterNotebooks/Robinhood/Robinhood/tickers.csv')
        tickers = tickers.symbols.to_list()
        for ticker in tickers:
            url = 'https://robinhood.com/stocks/' + ticker
            yield Request(url =  url ,callback = self.parse_result_page, meta = {'ticker':ticker})

    def parse_result_page(self, response):
        Company_Name = response.xpath('//header[@class="Jo5RGrWjFiX_iyW3gMLsy"]//text()').extract_first()
        Market_Price = response.xpath('//div[@class="QzVHcLdwl2CEuEMpTUFaj"]//text()').extract()
        Headquarters = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[5]
        Employees = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[3]
        PE_Ratio = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[11]
        Market_Cap = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[9]
        Dividend_Yield = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[13]
        Average_Volume = response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[15]
        Collections = response.xpath('//div[@class="_1gfDwaPob6nH6DaLh22jJc GqrlJFCP9dGyABby0KoOo"]//text()').extract()
        Ratings = response.xpath('//div[@class="_1fEdz1YPOLpLW1Ow3rKh92"]//text()').extract()
        Buy_Hold_Sell = response.xpath('//div[@class="_14n7Un633WYtQAVrDNl0J3"]//text()').extract()

        item = RobinhoodItems()
        item['Symbol'] = response.meta['ticker']
        item['Company_Name'] = Company_Name
        item['Headquarters'] = Headquarters
        item['Market_Price'] = Market_Price
        item['Employees'] = Employees
        item['PE_Ratio'] = PE_Ratio
        item['Market_Cap'] = Market_Cap
        item['Dividend_Yield'] = Dividend_Yield
        item['Average_Volume'] = Average_Volume
        item['Collections'] = Collections
        item['Ratings'] = Ratings
        item['Buy_Hold_Sell'] = Buy_Hold_Sell
        yield item