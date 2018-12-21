from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tifico',
    url='https://github.com/smartninja/tifico',
    author='Matej Ramuta',
    author_email='matej.ramuta@gmail.com',
    packages=['tifico'],
    install_requires=[
        'tinydb==3.12.2',
    ],
    version='0.1',
    license='MIT',
    description='Tifico - a simple ODM for three NoSQL databases: TinyDB, Firestore and Cosmos DB (via PyMongo API).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
