from distutils.core import setup

setup(
    name='mailnagger',
    version='0.1dev',
    packages=['MailNagger',],
    license='DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE',
    long_description=open('README.md').read(), requires=['googleapiclient', 'google', 'pytest']
)