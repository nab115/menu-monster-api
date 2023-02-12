from pymongo import MongoClient

def get_db_client(username, password):
    
    connection_string = 'mongodb+srv://{username}:{password}@menuitems.wdbco70.mongodb.net/?retryWrites=true&w=majority'.format(
        username=username
        , password=password
    )

    return MongoClient(connection_string)