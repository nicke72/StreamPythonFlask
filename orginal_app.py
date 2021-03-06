#!/usr/bin/env python
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
            #for i, c in enumerate(itertools.cycle('\|/-')):
            #    yield "data: %s %d\n\n" % (c, i)
            #    time.sleep(1)  # an artificial delay
	    c = random.randint(1, 2000)
	    yield "data: %s\n\n" % (c)
	    time.sleep(5)
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

