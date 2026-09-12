import json
from collections import Counter
from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["GitHubArchiveDB"]
collection = db["Commits"]


# Load JSON data into MongoDB
def load_data():
    try:
        with open("GitHubArchive-Dataset/Commits.json", "r", encoding="utf-8") as file:

            for line in file:
                data = json.loads(line)

                collection.insert_one(data)

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("Commits.json was not found.")


# CREATE
def create_commit():

    print("\nCreate Commit")

    commit_id = input("Enter commit ID: ")
    author_name = input("Enter author name: ")
    author_email = input("Enter author email: ")
    repo_name = input("Enter repository name: ")
    message = input("Enter commit message: ")

    new_commit = {
        "commit": commit_id,

        "author": {
            "name": author_name,
            "email": author_email
        },

        "repo_name": repo_name,

        "message": message,

        "subject": message
    }

    collection.insert_one(new_commit)

    print("Commit added successfully.")


# READ
def read_commit():

    print("\nRead Commit")

    commit_id = input("Enter commit ID: ")

    result = collection.find_one({
        "commit": commit_id
    })

    if result:
        print("\nCommit Found:")
        print(result)

    else:
        print("Commit not found.")


# UPDATE
def update_commit():

    print("\nUpdate Commit")

    commit_id = input("Enter commit ID: ")

    result = collection.find_one({
        "commit": commit_id
    })

    if result:

        new_message = input("Enter new commit message: ")

        collection.update_one(
            {"commit": commit_id},
            {
                "$set": {
                    "message": new_message,
                    "subject": new_message
                }
            }
        )

        print("Commit updated successfully.")

    else:
        print("Commit not found.")


# DELETE
def delete_commit():

    print("\nDelete Commit")

    commit_id = input("Enter commit ID: ")

    result = collection.delete_one({
        "commit": commit_id
    })

    if result.deleted_count > 0:
        print("Commit deleted successfully.")

    else:
        print("Commit not found.")


# FEATURE 1
# Find longest and shortest repository names
def repository_names():

    repo_names = []

    results = collection.find({}, {"repo_name": 1})

    for record in results:

        if "repo_name" in record:

            repo = record["repo_name"]

            # Some records store repo_name as a list
            if isinstance(repo, list):

                for name in repo:
                    repo_names.append(name)

            else:
                repo_names.append(repo)

    if len(repo_names) > 0:

        longest = max(repo_names, key=len)
        shortest = min(repo_names, key=len)

        print("\nLongest Repository Name:")
        print(longest)

        print("\nShortest Repository Name:")
        print(shortest)

    else:
        print("No repository names found.")


# FEATURE 2
# Display most common repositories
def popular_repositories():

    repo_names = []

    results = collection.find({}, {"repo_name": 1})

    for record in results:

        if "repo_name" in record:

            repo = record["repo_name"]

            if isinstance(repo, list):

                for name in repo:
                    repo_names.append(name)

            else:
                repo_names.append(repo)

    counts = Counter(repo_names)

    print("\nMost Common Repositories:")

    for repo, count in counts.most_common(10):
        print(repo, "-", count)


# FEATURE 3
# Find common words in commit messages
def common_words():

    words = []

    results = collection.find({}, {"message": 1})

    for record in results:

        if "message" in record:

            message = record["message"].lower()

            message_words = message.split()

            for word in message_words:

                word = word.strip(".,!?():;[]{}")

                if len(word) > 3:
                    words.append(word)

    counts = Counter(words)

    print("\nMost Common Commit Message Words:")

    for word, count in counts.most_common(10):
        print(word, "-", count)


# Display database information
def database_info():

    total = collection.count_documents({})

    print("\nDatabase:", db.name)
    print("Collection:", collection.name)
    print("Total Records:", total)


# Main menu
def main():

    while True:

        print("\n----------------------------")
        print("GitHub Archive Application")
        print("----------------------------")

        print("1. Load JSON Data")
        print("2. Create Commit")
        print("3. Read Commit")
        print("4. Update Commit")
        print("5. Delete Commit")
        print("6. Longest and Shortest Repository")
        print("7. Most Common Repositories")
        print("8. Most Common Commit Words")
        print("9. Database Information")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            load_data()

        elif choice == "2":
            create_commit()

        elif choice == "3":
            read_commit()

        elif choice == "4":
            update_commit()

        elif choice == "5":
            delete_commit()

        elif choice == "6":
            repository_names()

        elif choice == "7":
            popular_repositories()

        elif choice == "8":
            common_words()

        elif choice == "9":
            database_info()

        elif choice == "0":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


main()
