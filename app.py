#!/usr/bin/env python

import sys
import packetlogic2
import itertools
import random
import time
from flask import Flask, Response, redirect, request, url_for

app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
	    host = "172.17.0.9"
	    user = "plview"
            pwd = "plview"
            path = "/NetObjects/All_Traffic"
            try:
              pl = packetlogic2.connect(host, user, pwd)
            except:
              t, v, tb = sys.exc_info()
              print "Error: Couldn't connect: %s" % v
              sys.exit(1)
            rt = pl.Realtime()



            #for i, c in enumerate(itertools.cycle('\|/-')):
            #    yield "data: %s %d\n\n" % (c, i)
            #    time.sleep(1)  # an artificial delay
	    #c = random.randint(1, 2000)
            file = open('newfile.txt', 'r')
	    c = file.readline( )
	    yield "data: %s\n\n" % (c)
	    time.sleep(2)
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

