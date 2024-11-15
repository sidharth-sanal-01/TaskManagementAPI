from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from pymongo.server_api import ServerApi
import asyncio


class Database:
    # initialized the database with database url and database name
    def __init__(self, database_url, database_name):
        self.database_url = database_url
        self.database_name = database_name

    # get the client setup for each request..Earlier we tried this with
    # by creating direclty in initialization but it was showing some thread errors
    # so this approach will create a connection for each request
    def get_client(self):
        return AsyncIOMotorClient(self.database_url, server_api=ServerApi("1"))

    # for internal functions to use database
    def get_database(self):
        return AsyncIOMotorClient(self.database_url, server_api=ServerApi("1"))[
            self.database_name
        ]

    # This function will call the async function that can list database names
    def show_databases(self):
        names = asyncio.run(self.list_databases())
        print(names)

    # this function will call the async function that can list the collection names
    def show_collections(self):
        collections = asyncio.run(self.list_collections())
        return collections

    # this function can check and remove collections based on whether it is present
    # in our system or not
    def check_and_remove_collection(self,collection_name):
        if collection_name not in self.show_collections():
            print("Invalid Collection name...Collection not preset in database..")
        else:
            print("Before Deletion: ",self.show_collections())
            asyncio.run(self.remove_collection(collection_name))
            print(f"Deleted collection {collection_name} Successfully")
            print("After Deletion: ", self.show_collections())

    # this function will check and add collections based on whether it is present in
    # our system or not
    def check_and_add_collections(self, collection_names):
        for collection in collection_names:
            if collection not in self.show_collections():
                asyncio.run(self.add_collection(collection))
            else:
                print(f"Collection {collection} Already Present..")
                # print(self.show_collections())

    # this function will add the collection to the database but it has
    # to be called with async.run() since it is a async function
    async def add_collection(self, collection_name):
        await self.get_database().create_collection(collection_name)

    # this function will remove the collection to the database but it has
    # to be called with async.run() since it is a async function
    async def remove_collection(self,collection_name):
        await self.get_database().drop_collection(collection_name)

    # this function will list all the collection on the database but it has
    # to be called with async.run() since it is a async function
    async def list_collections(self):
        collections = await self.get_client()[
            self.database_name
        ].list_collection_names()
        return collections

    # this function will list all the databases on the connection but it has
    # to be called with async.run() since it is a async function
    async def list_databases(self):
        names = await self.get_client().list_database_names()
        return names


db = Database(settings.database_url, settings.database_name)
db.show_databases()
db.show_databases()
print(db.show_collections())
print(db.show_collections())
db.check_and_add_collections(["Stories", "Tasks", "users"])
db.check_and_remove_collection("Stories")
# print(db.show_collections())
