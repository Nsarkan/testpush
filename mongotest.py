from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://nitishsarkar1234:Nitaidas100@cluster0.tf1votj.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



d={'name':'nitish','email':'nitish1234@gmail.com','surname':'sarkar'}

d={'name':'nitish','email':'nitish1234@gmail.com','surname':'sarkar'}

d={'name':'nitish','email':'nitish1234@gmail.com','surname':'sarkar'}


db=client['mongotest']
coll=db['test']
coll.insert_one(d)