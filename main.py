f = open('password.txt', 'r')
password = f.read().strip()
mydatabase="library" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor