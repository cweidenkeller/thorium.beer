from setuptools import setup, find_packages

setup(
    name = "thorium",
    version = "0.1",
    packages = find_packages(),
    scripts = [],
    install_requires = ['Flask==0.10.1',
                        'itsdangerous==0.24',
                        'Jinja2==2.8',
                        'MarkupSafe==0.23',
                        'Werkzeug==0.11.4',],
    author = "Thorium",
    author_email = "info@thorium.beer",
    url = "http://thorium.beer"
)
