from setuptools import setup, find_packages

setup(
    name='thorium',
    version='0.1',
    packages=find_packages(),
    scripts=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask==0.10.1', 'Flask-SQLAlchemy==2.1'],
    entry_points={'console_scripts' : ['thorium = thorium.run:run']},
    author="Thorium",
    author_email="info@thorium.beer",
    url="http://thorium.beer"
)
