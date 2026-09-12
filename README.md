# MongoDB-Integration
# Dalvin Wolff 
#DALWOL9523 ECPI University SDC435
# MongoDB Integration Project

## Dependencies

* Python 3
* PyMongo

Install PyMongo with:

`pip install pymongo`

## Technology Requirements

* Python
* MongoDB
* PyMongo
* GitHub
* JSON dataset from GitHub Archive

MongoDB must be installed and running locally before starting the application.

## Current Features

* Loads GitHub Archive JSON data into MongoDB
* Creates new commit records
* Reads commit records by commit ID
* Updates commit messages
* Deletes commit records
* Displays the longest and shortest repository names
* Displays the most common repositories
* Displays the most common words found in commit messages
* Displays basic database information

## Running the Program

1. Make sure MongoDB is running.
2. Place the `GitHubArchive-Dataset` folder in the project folder.
3. Install PyMongo.
4. Run `IntergrateMongo.py`.
5. Choose an option from the menu.

## Dataset Note

The GitHub Archive dataset is not included in the GitHub repository because of file-size limitations. The dataset should be placed in the project folder before running the application.
