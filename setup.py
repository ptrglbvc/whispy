#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='whispy',
      version='0.1',
      description='Basically a simple python cli tool for transcription, using the whisper model by openai',
      author='Petar Golubović',
      author_email='petar0golubovic@gmail.com',
      packages=find_packages(),
          entry_points={
              'console_scripts': [
                    'wh = src.whis.whisper:main',
              ],
         },
    )
