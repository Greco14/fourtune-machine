import web
from web.wsgiserver import CherryPyWSGIServer
from collections import defaultdict

import json
import shelve
import os

cdir = os.getcwd()
CherryPyWSGIServer.ssl_certificate = cdir + "/ssl/server.crt"
CherryPyWSGIServer.ssl_private_key = cdir + "/ssl/server.key"

DEBUG=0
FILE='/tmp/checkin'

urls = ("/.*", "savecheckin")
app = web.application(urls, globals())

class savecheckin:
    def GET(self):
        return 'Check In storage'

    def POST(self):
        form = json.loads(web.data())
        if form['type'] == 'checkin':
            s = shelve.open(FILE)
            if not 'checkins' in s:
                s['checkins'] = []
            ci = s['checkins']
            ci.append(1)
            s['checkins'] = ci
            s.close()
            return "Checked in"
        return 'Unknown command' 

if __name__ == "__main__":
    app.run()
