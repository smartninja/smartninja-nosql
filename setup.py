import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='smartninja-nosql',
    url='https://github.com/smartninja/smartninja-nosql',
    author='Matej Ramuta',
    author_email='matej.ramuta@gmail.com',
    packages=['smartninja_nosql'],
    install_requires=[
        'tinydb==3.12.2',
        'tinydb_serialization==1.0.4',
    ],
    version='0.6',
    license='MIT',
    description='SmartNinja NoSQL - a simple ODM for NoSQL databases: TinyDB, Firestore, Datastore, MongoDB and Cosmos DB.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
