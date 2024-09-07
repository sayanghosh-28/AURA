import mysql.connector as sqltor

mycon=sqltor.connect(host="localhost",user="root",passwd="sayan2801",database='sayan')
if mycon.is_connected():
    print("succesfull")

cursor=mycon.cursor()

'''query="CREATE TABLE IF NOT EXISTS web_commands(id integer primary key,name VARCHAR(50),path VARCHAR(1000))"
cursor.execute(query)'''

query="INSERT INTO web_commands VALUES(3,'chatgpt','https://chatgpt.com/')"
#query = r"UPDATE commands SET path='C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE' WHERE id=2"
cursor.execute(query)
mycon.commit()