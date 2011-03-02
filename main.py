from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import csshelper

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
        	csshelper.content().get(
        """
	     <div class="post">
	       <div class="header">Intro to app engine</div>
	       <div class="content">This walk-through should help you get off the ground with google app engine. Click on the QR Code menu to build your own QR Codes.</div>
	     </div>		  
	"""))
		   


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
