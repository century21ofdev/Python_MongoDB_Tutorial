from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # initialize with your URI
your_collection = client['_books']  # your collection string here

result = your_collection.aggregate([
    {'$match':
         {'$b_id': 101}
     },
    {'$group':
         {'_id': "$b_id", 'total_stock': {"$sum": "$stock"}}
     }
])

