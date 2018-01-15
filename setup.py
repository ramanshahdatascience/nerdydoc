from setuptools import setup

setup(name='nerdydoc',
      version='0.1',
      description='Build a Python documentation site from NumPy-style docstrings',
      url='http://github.com/ramanshah/nerdydoc',
      author='Raman A. Shah',
      author_email='raman.anand.shah@gmail.com',
      license='BSD3',
      packages=['nerdydoc'],
      entry_points={
          'console_scripts': ['nerdydoc=nerdydoc.main:main']},
      zip_safe=False)
