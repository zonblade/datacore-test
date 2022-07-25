from setuptools import setup

setup(
    name         = 'datacore',
    version      = '1', 
    author       = 'AgungZonBlade',
    author_email = 'agungzonblade@gmail.com',
    license      = 'LICENSE.txt',
    description  = 'An awesome package that does something',
    packages     = [
        'datacore',
        'datacore.http',
        'datacore.http.decorator',
        'datacore.http.decorator.asynclib',
        'datacore.utils',
        'datacore.utils.hashlib',
    ],
    install_requires=[
        'PyJWT',
        'Django'
    ]
)