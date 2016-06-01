import scrapy
from yattag import Doc, indent
import csv

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




# read the info
with open('subject_website.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            w_id = row[0]
            w_name = row[1]
            w_info1 = row[2]
            w_info2 = row[3]
            w_url = row[4]
            w_url_rss = 'http://www.myrss.com'
            # add a xml format
            #put in a xml
            doc, tag, text = Doc().tagtext()
            with tag('root'):
                with tag('doc'):
                    with tag('id', name='is'):
                        text(w_id)
                    with tag('name', name='name'):
                        text(w_name)
                    with tag('info1', name='info1'):
                        text(w_info1)
                    with tag('info2', name='info2'):
                        text(w_info2)
                    with tag('urlWeb', name='webSite'):
                        text(w_url)
                    with tag('urlRss', name='urlRss'):
                        text(w_url_rss)
            result = indent(
                doc.getvalue(),
                indentation = ' '*4,
                newline = '\r\n'
            )
            # end xml format
            filename = 'respuestas.xml'
            file = open(filename, 'rw+')
            file.seek(0, 2)
            #    file.writelines(qqq)
            file.write(result) # print the xml format
            file.writelines('\n')
            file.close()
print '---------------------------------------'
print '---------------------------------------'
