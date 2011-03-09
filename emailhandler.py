from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch

import urllib

import csshelper


class emailhandler(webapp.RequestHandler):
    def get(self):    	  
    	self.response.out.write(
    		csshelper.content().get(
        """
	<form action="/emsg" method="post">
	<div>Please fill in your email template:
	<table>
	<tr><td>To:</td><td> <input type="text" name="recipient" cols="75" /></td></tr>
	<tr><td>Subject:</td><td> <input type="text" name="subject" cols="75" /></td></tr>
	<tr><td>Body:</td><td> <textarea name="body" cols="60" rows="10"> </textarea></td></tr>
	<tr><td colspan="2"> <input type="submit" text="Go" /> </td></tr>
	</table>
	</div> </form>
	""" ))


    def post(self):
	recipient = self.request.get('recipient')
	subject = self.request.get('subject')
	body = self.request.get('body')

	email = 'MATMSG:TO:' + recipient + ';SUB:' + subject + ';BODY:' + body + ';;'

        content = urllib.quote(email)
	self.response.out.write( csshelper.content().get('<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([('/emsg', emailhandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
