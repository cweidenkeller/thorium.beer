from setuptools import setup, find_packages

setup(
    name='thorium',
    version='0.1',
    packages=find_packages(),
    scripts=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
                      'flake8==2.5.4',
                      'Flask==0.10.1',
                      'pylint==1.5.5',
                      'tox==2.3.1',]
    author="Thorium",
    author_email="info@thorium.beer",
    url="http://thorium.beer"
)
