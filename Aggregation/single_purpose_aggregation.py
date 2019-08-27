from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # initialize with your URI
your_collection = client['_books']  # your collection string here

# we can not do the single purpose aggregation directly by calling like yourcollection.distinct([{...}]]
# i have applied single purpose aggregation in MongoDB Compass, you can also too in mongo shell.

result = your_collection.aggregate([
    {'$match': {'status': 'A'}},  # matched with A that status has
    {'$group': {'_id': '$b_id', 'distinct_values': {'$addToSet': "$x"}}}
    # $addToSet provides that omit duplicate values.
])

print(list(result))
