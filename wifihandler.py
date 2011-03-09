from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch

import urllib

import csshelper


class wifihandler(webapp.RequestHandler):
    def uri(self):
    	return '/wifi'
    def get(self):    	  
    	self.response.out.write(
    		csshelper.content().get('<form action="' + self.uri() + '" method="post">' +
        """
	<div>Please fill in your WIFI setup information: 
	<table>
	<tr><td>Authentication Type: (WEP/WPA)</td><td> <input type="text" name="authtype" cols="15" /></td></tr>
	<tr><td>SSID:</td><td> <input type="text" name="ssid" cols="20" /></td></tr>
	<tr><td>Password:</td><td> <input type="password" name="password" cols="20" /></td></tr>
	<tr><td colspan="2"> <input type="submit" text="Go" /> </td></tr>
	</table>
	</div> </form>
	""" ))


    def post(self):
	authtype = self.request.get('authtype')
	ssid = self.request.get('ssid')
	password = self.request.get('password')
	
	wifidata = 'WIFI:T:' + authtype + ';S:' + ssid + ';P:' + password + ';;'

        content = urllib.quote(wifidata)
	self.response.out.write( csshelper.content().get('<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([(wifihandler().uri(), wifihandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
