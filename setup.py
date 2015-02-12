from setuptools import setup, find_packages
from setuptools.command.test import test as _test
#print(os.getcwd())
#response = urllib2.urlopen('http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz')
#file = response.read()
#with open('geoip/GeoLite2-City.mmdb', 'wb') as f:
#    f.write(file)

class test(_test):
    def finalize_options(self):
        _test.finalize_option(self)
        import geolite

setup(
    name='geolite',
    description='geolite database',
    packages=find_packages()
            )
