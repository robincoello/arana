import scrapy
from yattag import Doc, indent
import csv, csv

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = []   

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
	# uncoment to create a new file with a url from a csv

# the file where find a url to analize 
    #f = open("urls.txt")
  #  start_urls = [url.strip() for url in f.readlines()]
    #f.close()
    star_urls = w_url

'''
       # print w_url
	f = 'urls.txt'
        file = open(f, 'rw+')
        file.seek(0, 2)
        file.writelines(w_url + '\n') # test to try make a xml
        file.close()
'''
def parse(self, response):

	#file to save
    filename = 'respuestas.html'
    qqq = response.xpath("/html/head/link[@type='application/rss+xml']/@href").extract()        
    print '---------------------------------------'
    file = open(filename, 'rw+')
    file.seek(0, 2)
    #file.writelines(result) # test to try make a xml
    file.writelines(w_id,qqq) # uncoment this to write a rss
    file.close()
    print '---------------------------------------'
    print '---------------------------------------'


'''
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
'''










