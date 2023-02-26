from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'psycopg2-binary'
    ],
    entry_points={
        'console_scripts': [
            'myproject=myproject.cli:main'
        ]
    },
)
