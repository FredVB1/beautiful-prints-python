from setuptools import setup, find_packages

setup(
    name='beautiful-prints',
    version='0.1',
    url='https://github.com/FredVB1/print-nested-data-python.git',
    license='MIT',
    author='Frederic vB',
    description="An easy way to make beautiful prints of nested data in python",
    packages=find_packages(exclude=['examples']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False
)
