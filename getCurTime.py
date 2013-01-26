
import cookielib, urllib, urllib2
import time, sys

entryUrl = " http://202.117.122.8/patroninfo/ "
#entryUrl = "http://218.85.137.211:7003/xmll/login.do?area=xm"
checkUrl = "http://218.85.137.211:7003/xmll/loginSubmit.do"
cl = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cl))
urllib2.install_opener(opener)

para = {'code' : "00168338",
        'pin' : "199010",
       }

postData = urllib.urlencode(para)

#resp = urllib2.urlopen(entryUrl)
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = urllib2.Request(url = entryUrl, data = postData, headers = headers)

count = 1
while(True):

	next = urllib2.urlopen(req)		#open this page
	#TODO: get the time on the page
	print next.geturl()
	
	print "Login Count:%d" % count
	count = count+1
	print "Now time: ",
	cur_time = time.localtime();
	cur_min = cur_time.tm_min;
	print time.strftime("%a, %d %b %Y %H, %H:%M:%S ", cur_time)
	print "********************************"
	if(cur_min >= 25):
		break
	#print cur_time
	time.sleep(10)
