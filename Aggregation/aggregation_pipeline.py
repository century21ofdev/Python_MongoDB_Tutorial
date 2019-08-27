from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # initialize with your URI
your_collection = client['_books']  # your collection string here

result = your_collection.aggregate([
    {'$match': {'status': "A"}},
    {'$group': {'_id': "$b_id", 'total': {'$sum': "$stock"}}}
])

print(list(result))
