import pymongo
from bson import ObjectId


# CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

# CREATE DATABASE
database = connection['my_database']
# CREATE COLLECTION
collection = database['my_collection']
print("Database connected")




def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    print("Inside Insert")
    document = collection.insert_one(data)
    
    return document.inserted_id


def update_or_create(name, Regno):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({"Name": name}, {"$set":{"Regno":Regno}}, upsert=True)
    return document.acknowledged


def get_single_data(name):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    data = collection.find_one({"Name": name})
    return data


def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    data = collection.find()
    return list(data)


def update_existing(name, Regno):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({"Name": name}, {"$set":{"Regno":Regno}})
    return document.acknowledged


def remove_data(name):
    document = collection.delete_one({'Name': name})
    return document.acknowledged
if __name__ == "__main__":
	print("Hai")
	#print(insert_data({'_id':1,"Name": "abc", "Regno": "5678"}))
	#print(remove_data("vinu"))
	#print(get_single_data("xyz"))
	#update_or_create("xyz", "1111")
	#update_existing("abc", "0000")
	print("\n",get_multiple_data())

# CLOSE DATABASE
connection.close()
