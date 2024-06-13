from setuptools import setup, find_packages

setup(
    name='quad_db_api',
    version='0.1.0',
    description='Python wrapper for the QuadDB API',
    author='CyberDefenseEd',
    url='https://github.com/CyberDefenseEd/qdb.py',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
