from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Ollama-Call-AI-Server',
  version='1.0',
  description='easy to use client for calling a remote Ollama AI server',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='zanarian',
  author_email='aroonv@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='AI, Ollama, client, remote server, call ai', 
  packages=find_packages(),
  install_requires=['requests'] 
)