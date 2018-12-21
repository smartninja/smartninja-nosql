# Tifico ODM

## About

Tifico is a simple ODM tool which helps you switch between three NoSQL database systems: TinyDB, Firestore and Cosmos
DB (via MongoDB API). The name Tifico is made out of the first two letters of each of these databases (TInydb,
FIrestore, COsmos).

TinyDB is used for localhost development. The advantage is that it saves you time configuring a Firestore or Cosmos
emulator on localhost.

When you deploy your web app to Google Cloud or Azure, the ODM figures out the new environment (through env variables)
and switches the database accordingly.

Bear in mind that this is a simple ODM meant to be used at the SmartNinja courses for learning purposes. So not all
features of these NoSQL databases are covered, only the basic ones.

