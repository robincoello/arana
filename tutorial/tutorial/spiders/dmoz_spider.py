import scrapy
from yattag import Doc, indent

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
        doc, tag, text = Doc().tagtext()

        with tag('root'):
            with tag('doc'):
                with tag('url', name='web'):
                    text('web')
                with tag('url', name='rss'):
                    text('qqq')
        result = indent(
            doc.getvalue(),
            indentation = ' '*4,
            newline = '\r\n'
        )

        print '---------------------------------------'
        file = open(filename, 'rw+')
        file.seek(0, 2)
        file.writelines(result) # test to try make a xml
        #file.writelines(qqq) # uncoment this to write a rss
        file.close()
        print '---------------------------------------'
        print '---------------------------------------'











