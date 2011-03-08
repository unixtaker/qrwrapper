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
	<table>
	<tr><td>First:</td><td> <input type="text" name="fname" cols="75" /></td></tr>
	<tr><td>Last:</td><td> <input type="text" name="lname" cols="75" /></td></tr>
	<tr><td>Email:</td><td><input type="text" name="email" cols="75"/></td></tr>
	<tr><td>Mobile Phone:</td><td><input type="text" name="mphone" cols="75"/></td></tr>
	<tr><td>Address:</td><td><input type="text" name="address" cols="75"/></td></tr>
	<tr><td colspan="2"> <input type="submit" text="Go" /> </td></tr>
	</table>
	</div> </form>
	""" ))


    def post(self):
    	fname = self.request.get('fname')
    	lname = self.request.get('lname')
	email = self.request.get('email')
	mphone = self.request.get('mphone')
	address = self.request.get('address')

	vcard = 'BEGIN:VCARD'
	vcard = vcard + '\nVERSION:3.0' 
	vcard = vcard + '\nFN:' + fname + ' ' + lname
	vcard = vcard + '\nN:' + lname + ';' + fname 
	if len(email) > 0:
		vcard = vcard + '\nEMAIL;TYPE=PREF,INTERNET:' + email
	if len(mphone) > 0:
		vcard = vcard + '\nTEL;TYPE=CELL,VOICE:' + mphone
	if len(address) > 0:
		vcard = vcard + '\nADR;TYPE=HOME:' + address
	vcard = vcard + '\nEND:VCARD'

        content = urllib.quote(vcard)
	self.response.out.write( csshelper.content().get('<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([('/vc', vcardhandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
