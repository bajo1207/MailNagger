from distutils.core import setup

setup(
    name='app',
    version='0.1dev',
    packages=['app',],
    license='DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE',
    long_description=open('README.md').read(), requires=['googleapiclient', 'google', 'pytest']
)