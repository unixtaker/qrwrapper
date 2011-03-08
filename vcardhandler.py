from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch

import urllib

import csshelper


class vcardhandler(webapp.RequestHandler):
    def get(self):    	  
    	self.response.out.write(
    		csshelper.content().get(
        """
	<form action="/vc" method="post">
	<div>Put what you want your qr code to be here: 
	<input type="text" name="name" cols="75" />
	<input type="submit" text="Go" /></div> </form>
	""" ))


    def post(self):
    	name = self.request.get('name')
        content = urllib.quote('BEGIN:VCARD\nFN:' + name + '\nEMAIL;TYPE=PREF,INTERNET:test@home.net\nEND:VCARD')
	self.response.out.write( csshelper.content().get('<pre>' + content + '</pre>' + '<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([('/vc', vcardhandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
