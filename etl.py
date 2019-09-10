from etl.json_to_mongodb import JsonToMongoDB

if __name__ == '__main__':
    json_to_mongodb = JsonToMongoDB()
    json_to_mongodb.migrate()
