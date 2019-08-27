from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # initialize with your URI
your_collection = client['_books']  # your collection string here

result = your_collection.aggregate([
    {'$match': {'status': "A"}},  # adding first stage with $match function to filter the status field
    {'$group': {'_id': "$b_id", 'total': {'$sum': "$stock"}}}
    # grouped book_id fields as _id that indicates new total stock field
])

print(list(result))

"""
there is also a few stage type that we can use instead of $group or $match in case our needed
so that's why i highly recommend you to visit the below reference guide to get more information about that's

https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/
"""
