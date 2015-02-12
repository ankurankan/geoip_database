from setuptools import setup, find_packages
#print(os.getcwd())
#response = urllib2.urlopen('http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz')
#file = response.read()
#with open('geoip/GeoLite2-City.mmdb', 'wb') as f:
#    f.write(file)
setup(
    name='geolite',
    description='geolite database',
    packages=find_packages()
            )
