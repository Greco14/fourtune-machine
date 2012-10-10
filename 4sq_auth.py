from urllib import urlencode, urlopen
import httplib
import web
import json

ENDPOINT="https://foursquare.com/oauth2/access_token"
MYURL="http://fourtune.hsmty.org/callback"
USER_ID=""
SECRET=""

urls = (
    "/", "redirect",
    "/callback", "callback"
    )

app = web.application(urls, globals())

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
	    print res
        else:
            return 'Missing code parameter';

if __name__ == "__main__":
    app.run()
