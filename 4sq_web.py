import web
from web.wsgiserver import CherryPyWSGIServer
from collections import defaultdict

import json

CherryPyWSGIServer.ssl_certificate = "/tmp/cacert.pem"
CherryPyWSGIServer.ssl_private_key = "/tmp/server.pem"

DEBUG=0
FILE='/tmp/checkin'

cis = defaultdict(int);

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

    def POST(self):
    	input = web.input()
	form = json.loads(web.data())
	if form['type'] == 'checkin':
	    uid = 'user' + str(form['user']['id'])
	    cis[uid] += 1
	    file = open('w', FILE)
	    file.write('checkin')
	    file.close()
	    return "Count: " + str(cis[uid])
        return 'Unknown command' 

if __name__ == "__main__":
    app.run()
