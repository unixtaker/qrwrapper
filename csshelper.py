
class content(object):
	def get(self, content):
		return """
		<html>
		<head>
		<meta name="keywords" content="qr codes generator" />
		<meta name="description" content="" />
		<link rel="stylesheet" type="text/css" href="images/default.css" />
		</head>
		<body>
		<div id="outer">
		  <div id="upbg"></div>
		  <div id="inner">
		    <div id="header">
		      <h1>Houston Open Development
		      <sup>user group</sup></h1>		      		     
		    </div>
		    <div id="splash"></div>
		    """ + menu().get() + """ <!-- menu -->
		      
		     <div id="primarycontent">""" + content + """</div>
		     """ + footer().get() + """ <!-- footer -->
		   </div>
		</div>
		</body>
		</html>
		"""
		   


class menu(object):
	def get(self):
		return """
		<div id="menu">
		    <ul>
			<li class="first"><a href="/">Home</a></li>
			<li><a href="/qr">QR Code</a></li>
		    </ul>	
		</div>
    
		
"""		


class footer(object):
	def get(self):
		return """<div id="footer">
				&copy; 2011. Houston Open Development User Group. All rights reserved. Design by <a href="http://www.nodethirtythree.com/">NodeThirtyThree</a>.
				</div>				
"""
