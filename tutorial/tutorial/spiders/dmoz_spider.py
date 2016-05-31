import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = []

    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
 

    def parse(self, response):
        urlsrss = []
	#file to save
        filename = 'respuestas.html'
	qqq = response.xpath("/html/head/link[@type='application/rss+xml']/@href").extract()        
        urlsrss.append(qqq)
        print '---------------------------------------'
        print '--------antes de imprimir--------------'
        print urlsrss # just for check 
        print '---------------------------------------'
        print '---------------------------------------'
        print '---------------------------------------'
        with open(filename, 'wb') as f:
            f.writelines(qqq)

        print '----despues de imprimir ---------------'
        print '---------------------------------------'
        print "the url "
        print urlsrss
        print '---------------------------------------'
        print '---------------------------------------'
        print '---------------------------------------'
        print '--------The last line------------------'

