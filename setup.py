from setuptools import setup

setup(name='awair',
      version='0.0.2',
      description='A python wrapper for Awair private API',
      url='https://github.com/ybbarng/awair',
      auther='ybbarng',
      auther_email='ybbarng@gmail.com',
      license='MIT',
      packages=['awair'],
      install_requires=[
          'pytz',
          'requests',
      ],
      zip_safe=False)
