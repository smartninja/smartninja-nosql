import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tifimo',
    url='https://github.com/smartninja/tifimo',
    author='Matej Ramuta',
    author_email='matej.ramuta@gmail.com',
    packages=['tifimo'],
    install_requires=[
        'tinydb==3.12.2',
        'tinydb_serialization==1.0.4',
    ],
    version='0.3',
    license='MIT',
    description='Tifimo - a simple ODM for NoSQL databases: TinyDB, Firestore, MongoDB and Cosmos DB.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
