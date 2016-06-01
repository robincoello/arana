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
        print '---------------------------------------'
# add a xml format
        doc, tag, text = Doc().tagtext()

        with tag('root'):
            with tag('doc'):
                with tag('id', name='web'):
                    text('web')
                with tag('name', name='rss'):
                    text('qqq')
                with tag('info1', name='rss'):
                    text('qqq')
                with tag('info2', name='rss'):
                    text('qqq')
                with tag('url', name='rss'):
                    text('qqq')
        result = indent(
            doc.getvalue(),
            indentation = ' '*4,
            newline = '\r\n'
        )
# end xml format

        file = open(filename, 'rw+')
        file.seek(0, 2)
#        file.writelines(qqq)
        file.write(result) # print the xml format
        file.writelines('\n')
        file.close()
        print '---------------------------------------'
        print '---------------------------------------'
