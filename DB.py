import mysql.connector

def updateTraffic(trafficOnRoad12, trafficOnRoad34):
	
    ROAD = databaseConnection()
    myCursor = ROAD.cursor()
        
    trafficOnRoad1 = trafficOnRoad12[0]
    trafficOnRoad2 = trafficOnRoad12[1]
    trafficOnRoad3 = trafficOnRoad34[0]
    trafficOnRoad4 = trafficOnRoad34[1]
        
    myCursor.callproc('updateTrafficDensity',[trafficOnRoad1, trafficOnRoad2, trafficOnRoad3, trafficOnRoad4])
    ROAD.commit()
    
def getMax():
    ROAD = databaseConnection()
    mycursor = ROAD.cursor()
    mycursor.callproc('getMaximumTrafficDensity')
    return getResult(mycursor)
	
	
def checkMax(ID):
    ROAD = databaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('checkTrafficOnRoadwithID',[ID,])
    return getResult(myCursor)

def databaseConnection():
    mydb = mysql.connector.connect(
    host="192.168.1.15",
    user="root",
    passwd="root",
    database = "trafficdata",
    auth_plugin='mysql_native_password'
    )
    return mydb;

def getResult(cursor):
    for result in cursor.stored_results():
        res = result.fetchall()
        for x in res:
            return int(x[0])
