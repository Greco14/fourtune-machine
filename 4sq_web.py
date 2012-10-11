import web
from web.wsgiserver import CherryPyWSGIServer
from collections import defaultdict

from urllib import urlencode, urlopen
import json
import shelve
import os

ENDPOINT="https://foursquare.com/oauth2/access_token"
MYURL="http://fourtune.hsmty.org/callback"
USER_ID=""
SECRET=""

cdir = os.getcwd()
CherryPyWSGIServer.ssl_certificate = cdir + "/ssl/server.crt"
CherryPyWSGIServer.ssl_private_key = cdir + "/ssl/server.key"

urls = (
    "/", "redirect",
    "/callback", "callback"
    )

DEBUG=0
FILE='/tmp/checkin'

urls = (
    "/", "savecheckin",
    "/auth", "redirect",
    "/callback", "callback"
    )

app = web.application(urls, globals())

class savecheckin:
    def GET(self):
        return 'Check In storage'

    def POST(self):
        form =  web.data()
        if form.find('checkin') == 0:
            s = shelve.open(FILE)
            if not 'checkins' in s:
                s['checkins'] = []
            ci = s['checkins']
            ci.append(1)
            s['checkins'] = ci
            s.close()
            return "Checked in"
        return 'Unknown command' 

class redirect:
    def GET(self):
	query = urlencode((
	    ('client_id', USER_ID),
	    ('response_type', 'code'),
	    ('redirect_uri', MYURL)
	    ))
        raise web.redirect(
	    'https://foursquare.com/oauth2/authenticate?' + query,
            '301 Moved Permanently'
            )

class callback:
    def GET(self):
        # validation code
        query = web.input(code=None,fsqCallback=None)
        if query.code:
            query = urlencode((
		        ('client_id', USER_ID),
        		('client_secret', SECRET),
	        	('grant_type', 'authorization_code'),
        		('redirect_uri', MYURL),
        		('code', query.code)
        		))
            res = urlopen(ENDPOINT +'?'+ query)
            raise web.redirect(
	            'www.fourtunemachine.com/app',
                '301 Moved Permanently'
            )
        else:
            return 'Missing code parameter';


if __name__ == "__main__":
    app.run()
