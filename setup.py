from distutils.core import setup

setup(
    name='micromeritics',
    version='0.1.2dev',
    packages=['micromeritics',],
    maintainer='Stefan Koch',
    description='Python package for gas adsorption calculations and support tools.',
    maintainer_email='stefan.koch.micro@gmail.com', 
    url='https://github.com/Micromeritics/micromeritics',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    long_description=open('README.md').read(),
)
