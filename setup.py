from distutils.core import setup

setup(name='django-battlenet',
      license='MIT',
      version='0.0.3',
      packages=['battlenet',
                'battlenet.oauth2',
                'battlenet.community',
                'battlenet.community.d3',
                'battlenet.community.sc2',
                'battlenet.community.wow', ],
      description='API wrapper for Blizzards Community REST APIs & OAuth2 login',
      author='Chris Gibson',
      author_email='chris@chrisgibson.io',
      url='https://github.com/chrisgibson17/django-battlenet-oauth2',
      download_url='https://github.com/chrisgibson17/django-battlenet-oauth2/archive/master.tar.gz',
      install_requires=['requests', 'requests_oauthlib']
)
