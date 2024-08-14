# 0x01. NoSQL

## Back-end | NoSQL | MongoDB

### Project Overview
- **Start Date:** August 12, 2024, 6:00 AM
- **End Date:** August 14, 2024, 6:00 AM
- **Checker Release:** August 12, 2024, 6:00 PM
- **Auto Review:** At the deadline

### Resources
- [NoSQL Databases Explained](https://example.com)
- [What is NoSQL?](https://example.com)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://example.com)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://example.com)
- [Aggregation](https://example.com)
- [Introduction to MongoDB and Python](https://example.com)
- [mongo Shell Methods](https://example.com)
- [Mongosh](https://example.com)

### Learning Objectives
By the end of this project, you should be able to explain the following without external help:
- What NoSQL means
- Differences between SQL and NoSQL
- What ACID is
- What document storage is
- Types of NoSQL databases
- Benefits of NoSQL databases
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

### Requirements

#### MongoDB Command File
- Files interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- Files should end with a new line
- First line of all files should be a comment: `// my comment`
- A `README.md` file at the root of the project folder is mandatory
- File length will be tested using `wc`

#### Python Scripts
- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10
- Files should end with a new line
- First line of all files should be `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow `pycodestyle` style (version 2.5.*)
- File length will be tested using `wc`
- All modules should have documentation
- All functions should have documentation
- Code should not execute when imported (use `if __name__ == "__main__":`)

### Installation Guide

#### Install MongoDB 4.2 on Ubuntu 18.04
```sh
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```



## Tasks To Complete

+ [x] 0. **List all databases**<br/>[0-list_databases](0-list_databases) contains a MongoDB script that lists all databases in MongoDB.

+ [x] 1. **Create a database**<br/>[1-use_or_create_database](1-use_or_create_database) contains a MongoDB script that creates or uses the database `my_db`.

+ [x] 2. **Insert document**<br/>[2-insert](2-insert) contains a MongoDB script that inserts a document in the collection `school`:
  + The document must have one attribute `name` with value “Holberton school”.
  + The database name will be passed as an option of `mongo` command.

+ [x] 3. **All documents**<br/>[3-all](3-all) contains a MongoDB script that lists all documents in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 4. **All matches**<br/>[4-match](4-match) contains a MongoDB script that lists all documents with `name="Holberton school"` in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 5. **Count**<br/>[5-count](5-count) contains a MongoDB script that displays the number of documents in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 6. **Update**<br/>[6-update](6-update) contains a MongoDB script that adds a new attribute to a document in the collection `school`:
  + The script should update only document with `name="Holberton school"` (all of them).
  + The update should add the attribute `address` with the value “972 Mission street”.
  + The database name will be passed as an option of `mongo` command.

+ [x] 7. **Delete by match**<br/>[7-delete](7-delete) contains a MongoDB script that deletes all documents with `name="Holberton school"` in the collection `school`:
  + The database name will be passed as an option of `mongo` command.

+ [x] 8. **List all documents in Python**<br/>[8-all.py](8-all.py) contains a Python function that lists all documents in a collection:
  + Prototype: `def list_all(mongo_collection):`.
  + Return an empty list if no document in the collection.
  + mongo_collection will be the pymongo collection object.

+ [x] 9. **Insert a document in Python**<br/>[9-insert_school.py](9-insert_school.py) contains a Python function that inserts a new document in a collection based on `kwargs`:
  + Prototype: `def insert_school(mongo_collection, **kwargs):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + Returns the new `_id`.

+ [x] 10. **Change school topics**<br/>[10-update_topics.py](10-update_topics.py) contains a Python function that changes all topics of a school document based on the name:
  + Prototype: `def update_topics(mongo_collection, name, topics):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + `name` (string) will be the school name to update.
  + `topics` (list of strings) will be the list of topics approached in the school.

+ [x] 11. **Where can I learn Python?**<br/>[11-schools_by_topic.py](11-schools_by_topic.py) contains a Python function that returns the list of school having a specific topic:
  + Prototype: `def schools_by_topic(mongo_collection, topic):`.
  + `mongo_collection` will be the `pymongo` collection object.
  + `topic` (string) will be topic searched.

+ [x] 12. **Log stats**<br/>[12-log_stats.py](12-log_stats.py) contains a Python script that provides some stats about Nginx logs stored in MongoDB:
  + Database: `logs`.
  + Collection: `nginx`.
  + Display:
    + First line: `x logs` where `x` is the number of documents in this collection.
    + Second line: `Methods:`.
    + 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation at the start of each line).
    + One line with the number of documents with:
      + `method=GET`.
      + `path=/status`.
    + Example:
      ```log
      94778 logs
      Methods:
          method GET: 93842
          method POST: 229
          method PUT: 0
          method PATCH: 0
          method DELETE: 0
      47415 status check
      ```
  + You can use this dump as data sample: [dump.zip](dump.zip).

+ [x] 13. **Regex filter**<br/>[100-find](100-find) contains a MongoDB script that lists all documents with `name` starting by `Holberton` in the collection `school`:
  + The database name will be passed as an option of the `mongo` command.

+ [x] 14. **Top students**<br/>[101-students.py](101-students.py) contains a Python function that returns all students sorted by average score:
  + Prototype: `def top_students(mongo_collection):`.
    + `mongo_collection` will be the `pymongo` collection object.
  + The top must be in descending order of average score.
  + The average score must be part of each item returns with key = `averageScore`.
  + A sample document in the collection is shown below:
    ```json
    {
      "name": "Julia",
      "topics": [
        { "title": "Algo", "score": 10.5 },
        { "title": "C", "score": 10.2 },
        { "title": "Python", "score": 10.1 }
      ]
    }
    ```

+ [x] 15. **Log stats - new version**<br/>[102-log_stats.py](102-log_stats.py) improves [12-log_stats.py](12-log_stats.py) by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:
  + The top 10 IPs must be sorted.
     

     
## RESOURCES

+ [x] [NoSQL Databases Explained](https://intranet.alxswe.com/rltoken/wweK7dOY4pf8haCqv9Iv6Q)
+ [x] [What is NoSQL ?](https://intranet.alxswe.com/rltoken/QqqNmgzgwopHBv305ki6bg)
+ [x] [MongoDB with Python Crash Course - Tutorial for Beginners](https://intranet.alxswe.com/rltoken/RyyP9OH1EMBWWYpTs4TqoA)
+ [x] [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://intranet.alxswe.com/rltoken/9__3tR-NimgXlmjPQwTF-Q)
+ [x] [Aggregation](https://intranet.alxswe.com/rltoken/ziEDeniRobC6owPE1_avAQ)
+ [x] [Introduction to MongoDB and Python](https://intranet.alxswe.com/rltoken/axwwF4CjO7FnK8Ecochqnw)
+ [x] [mongo Shell Methods](https://intranet.alxswe.com/rltoken/lUqnLwOHbbp9FK39ijNmDQ)
+ [x] [The mongo Shell](https://intranet.alxswe.com/rltoken/bffQMLcTB4cg1bKqgBW3jw)   
