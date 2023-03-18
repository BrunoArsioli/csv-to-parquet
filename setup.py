from setuptools import setup

setup(
    name='csv-to-parquet',
    version='1.0',
    packages=['csv_to_parquet'],
    install_requires=[
        'pandas',
        'astropy'
    ],
    entry_points={
        'console_scripts': [
            'csv-to-parquet=csv_to_parquet.csv_to_parquet:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
