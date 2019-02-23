import pandas as pd
import urllib.request as urllib2

def check():
	counter = 0
	url = 'https://www.statsf1.com/en/2017.aspx'
	response = urllib2.urlopen(url)
	html = response.read()
	text = 'class="pays"'
	for line in html:
		if text in line:
			counter += 1
	return counter 

# print(check())
# print(html)

url = 'https://www.statsf1.com/en/2017.aspx'
response = urllib2.urlopen(url)
html = response.read()
print(type(html))
html = str(html, 'utf-8')
print(type(html))
total = html.count('class="pays"')
start = 0
f = open('test.txt', 'w+')
for i in range(total):
	start = html.find('class="pays"', start)
	start = html.find('.', start)
	end = html.find('<', start)
	f.write(html[start+2:end-1]+'\n') 
	

