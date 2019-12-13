from setuptools import setup

setup(
    name='epa-data',
    version='0.1',
    author='Jarret Minkler',
    author_email='jarret.minkler@gmail.com',
    description='Tool to scrape EPA Registration # information from various states',
    license='MIT',
    packages=['epa'],
    url='https://github.com/jminkler/epa',
    install_requires = [
        'click',
        'scrapy'
    ],
    entry_points='''
        [console_scripts]
        epa=epa.epa:cli
    ''',

)
