import urllib, requests

def login(url, user, passw):
    params = urllib.urlencode({'login:username': user, 'login:password': passw, 'login:j_id9': 'Entrar', 'javax.faces.ViewState': 'j_id1', 'login': 'login'})
    html = urllib.urlopen(url, params).read()
    return html

def logout():
    url  = "http://urlJavaApplication/logout.seam"
    html = urllib.urlopen(url).read()
    print (html)

def generateHtml(html):
	with open('./result.html','w+') as file:
		file.write(html)
	
def getSessionCookie():
	session = requests.Session()
	reponse = session.get('http://urlJavaApplication/login')
	return session.cookies.get('JSESSIONID')


url  = "http://urlJavaApplication/login;jsessionid="+getSessionCookie()
user  = 'userAccount'
passw = 'userPassword'

# LOGIN
html = login(url, user, passw)
generateHtml(html)

#LOGOUT
logout()