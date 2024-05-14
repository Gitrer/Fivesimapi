#!/usr/bin/env python

from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='5simapi',
  version='1.0.0',
  author='Gitrer',
  author_email='vadimbagaev462@gmail.com',
  description='This library is designed for simplified interaction with the API of the 5sim website',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='link',
  packages=find_packages(),
  install_requires=['requests'],
  classifiers=[
    'Programming Language :: Python :: 3.11.5',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'https://5sim.biz/docs'
  },
  python_requires='>=3.7'
)
