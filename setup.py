'''
Created on 27 Feb 2017

@author: vikas
'''
from setuptools import setup

setup(name="ledtester",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Vikas Leonard John",
      author_email="vikasleonard.john@ucdconnect.ie",
      licence="GPL3",
      packages=['src'],
      entry_points={
        'console_scripts':['ledtester=src.main:main']
        },
      install_requires=[
          'numpy',
      ],
      )