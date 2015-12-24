from setuptools import setup

setup(
    name='autoremote',
    version='0.1',
    license='MIT',
    author='Dan Yeakley',
    author_email='ddyeakley@gmail.com',
    url='https://github.com/ddyeakley/autoremote',
    long_description="README.txt",
    packages=['autoremote'],
    include_package_data=False,
    description="Simple Python tool to use autoremote to send data to a phone running tasker.",
)