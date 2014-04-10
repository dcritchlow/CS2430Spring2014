#!/usr/bin/python


import mechanize
import cookielib

file = 'download.html'
# url = 'http://www.kayak.com/flights/SLC-LAS/2014-03-19/2014-03-21'
# response = urllib2.urlopen(url)
# html = response.read()
# fh = open(file, 'w')
# fh.write(html)
# fh.close()
# response.close()

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open some site, let's pick a random one, the first that pops in mind:
url = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&TO=EUR'
r = br.open(url)
html = r.read()

# Show the source
print html
# # or
# print br.response().read()

# # Show the html title
# print br.title()

# # Show the response headers
# print r.info()
# # or
# print br.response().info()

# # Show the available forms
# for f in br.forms():
#     print f

# Select the first (index zero) form
# br.select_form(nr=0)

# br.form['origin']='SLC'
# br.form['destination']='LAS'
# br.form['depart_date']='2014-03-19'
# br.form['return_date']='2014-03-21'
# br.submit()

# # Let's search
# br.form['q']='weekend codes'
# br.submit()
# print br.response().read()

# Looking at some results in link format
# for l in br.links(url_regex='stockrt'):
#     print l
# for l in br.links():
#     print l.text, l.url
