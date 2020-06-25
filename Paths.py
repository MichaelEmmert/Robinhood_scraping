#buy,hold,sell list
class="_14n7Un633WYtQAVrDNl0J3"
response.xpath('//div[@class="_14n7Un633WYtQAVrDNl0J3"]//text()').extract()

# number of raters
class="_1fEdz1YPOLpLW1Ow3rKh92"
response.xpath('//div[@class="_1fEdz1YPOLpLW1Ow3rKh92"]//text()').extract()

#collections section (what groups the company is in)
class="_1gfDwaPob6nH6DaLh22jJc GqrlJFCP9dGyABby0KoOo"
response.xpath('//div[@class="_1gfDwaPob6nH6DaLh22jJc GqrlJFCP9dGyABby0KoOo"]//text()').extract()

# Stock price - long string
class="QzVHcLdwl2CEuEMpTUFaj"
response.xpath('//div[@class="QzVHcLdwl2CEuEMpTUFaj"]//text()').extract()

#company name
class="Jo5RGrWjFiX_iyW3gMLsy"
response.xpath('//header[@class="Jo5RGrWjFiX_iyW3gMLsy"]//text()').extract_first()

## Company information
class="_2SYphfY1DF71e5bReqgDyP"
response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()

response.xpath('//div[@class="_2SYphfY1DF71e5bReqgDyP"]//text()').extract()[3]

###
class="css-1npjp1l"
response.xpath('//div[@class="css-1npjp1l"]//text()').extract()
response.xpath('//span[@class="css-1npjp1l"]//text()').extract_first().split(' ')[1]
