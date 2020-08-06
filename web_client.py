
# web "client" fetches web page, given a url
## when asked, it checks its cache for the web page

# first request: fetches from the interwebz
# second request: returns from the cache

# Why?
## Faster, increased speeds
## Decrease load on web server
## Security
## Cuts down calls to APIs

# hash table usage to make a web client cache?
## URL could be the key
## web page data could be the value

# problems with our naive implementation?
## every successful complex system will be found to have evolved from a simple system
## what if the actual page changes? Our data will be old - stale
## No size limitation - end up storing the internet

# How to solve these problems?
## How to solve stale data in the cache?

import urllib.request

url = 'https://www.google.com'


cache = {}

page = None

if url in cache:
    cache[url]

# if not, go fetch it
else:
    print('getting from server')

    # fetch the data
    resp = urllib.request.urlopen(url)
    data = resp.read()
    # put in the cache
    cache[url] = data