#!/usr/bin/python

import cgi
import cgitb
import shutil

# The subprocess module is new in 2.4
import os, urllib, subprocess as sub


#cgitb.enable()
cgitb.enable(display=0, logdir="/var/www/log")

# Retrieve form fields
form   = cgi.FieldStorage()			# Get POST data

# Retrieve the command from the query string
# and unencode the escaped %xx chars
# str_command = urllib.unquote(os.environ['QUERY_STRING'])
output="" + form.keys()[0]


print """\
Content-Type: text/html;charset=utf-8\n
<html><body>
<pre>
%s
</pre>
</body></html>
""" % (output)

