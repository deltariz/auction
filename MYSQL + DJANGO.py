import mysql.connector as mys
mycon=mys.connect(host='local host', user= , password=)
if mycon.is_connected():
    print('connected')
else:
    print('error')

mycur=mycon.cursor()
qu='create table items(No int(2) primary key, name varchar(15), image, description varchar(40), startingbid int(5),startdate date')
mycur.execute(qu)
mycon.commit()




    
