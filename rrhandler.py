from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import csshelper

# rick roll - :) thanks guys

class rrhandler(webapp.RequestHandler):
    def get(self):    	  
    	self.response.out.write(
    		csshelper.content().get(
        """
	<form action="/rr" method="post">
	<div>Put what you want your qr code to be here: 
	<input type="text" name="content" cols="160" />
	<input type="submit" text="Go" /></div> </form>
	""" ))


    def post(self):
        content = 'http://www.youtube.com/watch?v=oHg5SJYRHA0' 
    	self.response.out.write(    	
    		csshelper.content().get(
    		  '<h1>Your QR code</h1><img src="https://chart.googleapis.com/chart?chs=200x200&cht=qr&chl=' + content + '"  alt="QR Code"/>' ))	

	
application = webapp.WSGIApplication([('/rr', rrhandler)], debug=True)


def main():
	util.run_wsgi_app(application)
	

if __name__ == '__main__':
	main()
