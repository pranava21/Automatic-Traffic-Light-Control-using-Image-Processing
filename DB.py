import mysql.connector


def updateTraffic(trafficOnRoad12, trafficOnRoad34):
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()

    trafficOnRoad1 = trafficOnRoad12[0]
    trafficOnRoad2 = trafficOnRoad12[1]
    trafficOnRoad3 = trafficOnRoad34[0]
    trafficOnRoad4 = trafficOnRoad34[1]

    myCursor.callproc('updateTrafficDensity', [trafficOnRoad1, trafficOnRoad2, trafficOnRoad3, trafficOnRoad4])
    ROAD.commit()


def getMax():
    ROAD = getDatabaseConnection()
    mycursor = ROAD.cursor()
    mycursor.callproc('getMaximumTrafficDensity')
    return getResult(mycursor)


def checkMax(ID):
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('checkTrafficOnRoadwithID', [ID, ])
    return getResult(myCursor)


def getSecondHighest():
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('getSecondHighestTrafficDensity')
    return getResult(myCursor)


def getLeast():
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('getLeastTrafficDensity')
    return getResult(myCursor)


def getThirdHighest():
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('getThirdHighestTrafficDensity')
    return getResult(myCursor)


def getTrafficDensityinOrder(i):
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('getTrafficDensityinOrder', [i, ])
    return getResult(myCursor)


def getI():
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('getI')
    return getResult(myCursor)


def setI(i):
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('setI', [i, ])
    ROAD.commit()


def incrementI():
    ROAD = getDatabaseConnection()
    myCursor = ROAD.cursor()
    myCursor.callproc('incrementI')
    ROAD.commit()


def getDatabaseConnection():
    mydb = mysql.connector.connect(
        host="192.168.1.15",
        user="root",
        passwd="password",
        database="trafficdata"
    )
    return mydb


def getResult(cursor):
    for result in cursor.stored_results():
        res = result.fetchall()
        for x in res:
            return int(x[0])
