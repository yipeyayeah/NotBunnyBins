import pymongo
from datetime import datetime
from twilio.rest import Client
class bin:
    def __init__(self, location, latitude, longitude):
        self.id="BunnyBin0010"
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.source = "Raspberry Pi"


    def insertToDatabase(self,close_sate_doc, capacity):
        try:
            client = pymongo.MongoClient("mongodb+srv://newuser2:gundam589@mycluster2.j0hmg.mongodb.net/BunnyBin?retryWrites=true&w=majority")
            mydb = client["BunnyBins"]
            mycol = mydb["bindatas"]
            current_time = datetime.now()

            document = {
                "id": self.id,
                "location": self.location,
                "state": close_sate_doc,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "time": current_time,
                "binCapacity": capacity,
                "source": self.source
            }

            mycol.insert_one(document)
        except Exception as e:
            print("An exception occurred ::", e)

    def triggerSMSToCleaner(self, mobile_number):
        account_sid = "AC35b622ad2fd3094dfd47f9b94e4ef723"
        auth_token = "90aec6c6a923a7050ff2392606f99efa"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+65"+str(mobile_number),
            from_="+16126885495",
            body="Bunny Bin at "+ self.location+" is filled! Please empty it. For more information visit www.facebook.com")

        print(message)
    def finf(self):
        client = pymongo.MongoClient("mongodb+srv://newuser2:gundam589@mycluster2.j0hmg.mongodb.net/BunnyBin?retryWrites=true&w=majority")
        mydb = client["BunnyBins"]
        mycol = mydb["bindatas"]
        for x in mycol.find():
            print(x)

location="Compass One Gideon was here!!!"
lat = 1.3924
long = 103.8954

sengkangBin = bin(location, lat, long)
sengkangBin.insertToDatabase("Open", 90)
# sengkangBin.triggerSMSToCleaner(96388495)
#sengkangBin.finf()
print("done")