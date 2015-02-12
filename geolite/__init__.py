import os
path = os.getcwd()

response = urllib2.urlopen('http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz')
file = response.read()
with open(os.path.join(path, 'geoip/GeoLite2-City.mmdb', 'wb') as f:
    f.write(file)
