import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = []

    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
 
    def parse(self, response):
	#file to save
        filename = 'respuestas.html'
	qqq = response.xpath("/html/head/link[@type='application/rss+xml']/@href").extract()        
        print '---------------------------------------'
        print '---------------------------------------'
        file = open(filename, 'rw+')
        file.seek(0, 2)
        file.writelines(qqq)
        file.writelines('\n')
        file.close()
        print '---------------------------------------'
        print '---------------------------------------'

