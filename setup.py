from setuptools import setup, find_packages
from os.path import join, dirname
import ydownload

setup(
    name='ydownload',
    version=ydownload.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), "README.txt")).read(),
    
    entry_points={
        'console_scripts':
            [
                'ydownload = ydownload.core:print_message',
                'serve= ydownload.web:run_server',
            ]
        },

    install_requires=[
        'Flask>=3.0'
    ],

    include_package_data=True,
    test_suite='tests',
)


