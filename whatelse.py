#coding=utf-8
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import sys

#########################################################################
#
#	by xingfenxiaozhu
#	blog www.xingfenxiaozhu.com
#	description:check if there's any other website at the same webserver
#	
#
#########################################################################


data_url="http://s.tool.chinaz.com/same"
#referer
referer=data_url
if len(sys.argv)!=2:
	print "######################################################"
	print "##    usage: python whatelse.py www.baidu.com[ip]   ##"
	print "######################################################"
	exit()

#the ip or domain you want to search
#你想搜索的目标ip或者域名
target_url=sys.argv[1]

post_data={"s":target_url}

encoded_data=urllib.urlencode(post_data)

req=urllib2.Request(data_url,encoded_data)

req.add_header("Referer",referer)

req.add_header("Host",'s.tool.chinaz.com')

print "here we go!waiting....."

response=urllib2.urlopen(req)

content=response.read()
print "results as follow:"
try:
	soup=BeautifulSoup(content)

	content=soup.find(id="contenthtml")
	if len(content.text)==8:
		print 'nothing found'
	else:
		result=''
		for i in content.ul:
			print i.a.text
except Exception,e:

	print "Ops, Something goes wrong or being limited !!"
	
