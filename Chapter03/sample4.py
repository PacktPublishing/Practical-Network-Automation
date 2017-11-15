import MySQLdb

def getfreeip():
    # Open database connection
    db = MySQLdb.connect("testserver","user","pwd","networktable" )
    cursor = db.cursor()

    sql = "select top 1 from freeipaddress where isfree='true'"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for eachrow in results:
          freeip=eachrow[0]
          return (freeip)
    except:
       print "Error: unable to fetch data"
       return "error in accessing table"
    db.close()


print (getfreeip())
