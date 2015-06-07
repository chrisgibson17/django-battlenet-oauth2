from distutils.core import setup

setup(name='django-battlenet',
    license='MIT',
    version='0.0.3',
    py_modules=[''],
    packages=['battlenet', 'battlenet.oauth2', 'battlenet.community'],
    description='API wrapper for Blizzards Community REST APIs & oAuth2 login',
    author='Chris Gibson',
    author_email='chris@chrisgibson.io',
    url='https://github.com/chrisgibson17/django-battlenet-oauth2',
    download_url='https://github.com/chrisgibson17/django-battlenet-oauth2/archive/master.tar.gz',
)