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
                with tag('field1', name='blah'):
                    text('some value1')
                with tag('field2', name='asdfasd'):
                    text('some value2')
        result = indent(
            doc.getvalue(),
            indentation = ' '*4,
            newline = '\r\n'
        )

        print '---------------------------------------'
        file = open(filename, 'rw+')
        file.seek(0, 2)
        file.writelines(result)
        file.close()
        print '---------------------------------------'
        print '---------------------------------------'











