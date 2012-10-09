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
        query = '?client_id={1}&response_type=code&redirect_uri={2}'
        query = query.format(USER_ID, urlencode(MYURL))
        raise web.redirect('https://foursquare.com/oauth2/authenticate' + query)

class callback:
    def GET(self):
        # validation code
        query = web.input(code=None,fsqCallback=None)
        if query.code:
            req_query = '?client_id={1}'\
                '&client_secret={2}'\
                '&grant_type=authorization_code'\
                '&redirect_uri={3}'\
                '&code={4}'
            url = urlencode(MYURL)
            qstring = req_query.format(USER_ID, SECRET, url, query.code)
            res = urlopen(ENDPOINT + qstring)
        else:
            return 'Missing code parameter';

if __name__ == "__main__":
    app.run()
