from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch

import urllib

import csshelper


class bizcardhandler(webapp.RequestHandler):
    def get(self):    	  
    	self.response.out.write(
    		csshelper.content().get(
        """
	<form action="/vc" method="post">
	<div>Please fill in your business card information:
	<table>
	<tr><td>First:</td><td> <input type="text" name="fname" cols="75" /></td></tr>
	<tr><td>Last:</td><td> <input type="text" name="lname" cols="75" /></td></tr>
	<tr><td>Title:</td><td> <input type="text" name="title" cols="75" /></td></tr>
	<tr><td>Email:</td><td><input type="text" name="email" cols="75"/></td></tr>
	<tr><td>Work Phone:</td><td><input type="text" name="wphone" cols="75"/></td></tr>
	<tr><td>Address:</td><td><input type="text" name="address" cols="75"/></td></tr>
	<tr><td colspan="2"> <input type="submit" text="Go" /> </td></tr>
	</table>
	</div> </form>
	""" ))


    def post(self):
    	fname = self.request.get('fname')
    	lname = self.request.get('lname')
    	title = self.request.get('title')
	email = self.request.get('email')
	wphone = self.request.get('wphone')
	address = self.request.get('address')

	vcard = 'BIZCARD:'
	vcard += 'N:' + fname + ';'
	vcard += 'X:' + lname + ';'
	if len(title) > 0:
		vcard += 'T:' + title + ';'
	if len(email) > 0:
		vcard += 'E:' + email + ';'
	if len(wphone) > 0:
		vcard += 'B:+1' + wphone + ';'
	if len(address) > 0:
		vcard = vcard + 'A:' + address + ';'
	vcard += ';;'

        content = urllib.quote(vcard)
	self.response.out.write( csshelper.content().get('<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([('/bz', bizcardhandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
