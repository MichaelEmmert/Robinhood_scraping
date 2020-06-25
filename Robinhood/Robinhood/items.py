import scrapy

class RobinhoodItems(scrapy.Item):
    Company_Name = scrapy.Field()
    Symbol = scrapy.Field()
    Headquarters = scrapy.Field()
    Market_Price = scrapy.Field()
    Employees = scrapy.Field()
    Collections = scrapy.Field()
    PE_Ratio = scrapy.Field()
    Market_Cap = scrapy.Field()
    Dividend_Yield = scrapy.Field()
    Average_Volume = scrapy.Field()
    Ratings = scrapy.Field()
    Buy_Hold_Sell = scrapy.Field()
