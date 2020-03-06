import mysql.connector

def updateTraffic(trafficOnRoad12, trafficOnRoad34):
	
    ROAD = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="password",
    database = "trafficData"
    )

    myCursor = ROAD.cursor()
        
    trafficOnRoad1 = trafficOnRoad12[0]
    trafficOnRoad2 = trafficOnRoad12[1]
    trafficOnRoad3 = trafficOnRoad34[0]
    trafficOnRoad4 = trafficOnRoad34[1]
        
    updateRoad1 = "UPDATE road SET trafficCount = %s WHERE id = %s"
    data1 = (trafficOnRoad1, 1)
    myCursor.execute(updateRoad1,data1)
    ROAD.commit()

    updateRoad2 = "UPDATE road SET trafficCount = %s WHERE id = %s"
    data2 = (trafficOnRoad2, 2)
    myCursor.execute(updateRoad2,data2)
    ROAD.commit()

    updateRoad3 = "UPDATE road SET trafficCount = %s WHERE id = %s"
    data3 = (trafficOnRoad3, 3)
    myCursor.execute(updateRoad3,data3)
    ROAD.commit()

    updateRoad4 = "UPDATE road SET trafficCount = %s WHERE id = %s"
    data4 = (trafficOnRoad4, 4)
    myCursor.execute(updateRoad4,data4)
    ROAD.commit()
    
def getMax():
    ROAD = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="password",
    database = "trafficData"
    )
    
    mycursor = ROAD.cursor()
    mycursor.execute("SELECT id FROM road ORDER BY trafficCount DESC LIMIT 1")
    myresult = mycursor.fetchall()

    for x in myresult:
        maxTrafficRoad = (int(x[0]))

    return maxTrafficRoad
	
	
def checkMax(ID):
    ROAD = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="password",
    database = "trafficData"
    )

    myCursor = ROAD.cursor()

    sql = "SELECT trafficCount FROM road WHERE id = %s"
    maxT = (ID,)
    myCursor.execute(sql, maxT)

    myresult = myCursor.fetchall()

    for x in myresult:
        return (int(x[0]))
