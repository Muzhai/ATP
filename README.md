# ATP


0.wir use alternative_pyodbc!!!

1.Precondition when you want to run test.py

	1) install modul pyodbc in python 
	2) install modul folium in python 
	3) replace the connection information.
	4) SQL Server: 
	    a) create databace (Baum)
	5) run

    PS. for the remote connect you should change the setting of SQL Server
      
2.Class MSSQL:

    1) here the connection to database ist defined
    2) two general methodes (query, non query) ist defined in order to  excute SQL language
    
3.Funktion

	1) main(server host, username, password, database, default_table="baum_test")
	    Import database information and connect to the database
		default_table is a optional variable. This should be the table, which you wante to operate.
		This function will be return a connection
	
	2) creat_table(table_name)
		table_name : string
		create a table which include tag_id, device_id, GPS, date
		Table elements have been defined in advance. If you want to modify, you must modify this function itself.
	
	3) drop_table(table_name)
		table_name : string
		drop a table totally
		
	4) insert_table_batch(baum_list)
		insert batch information to the table 
		baum_list : list
		a datalist like [{baum1}, {buam2},...]. element of the list is a dictionary. Its key correspond to the column of the table
		
	5) insert_table(baum)
		insert single information to the table
		baum : dictionary, correspond to the table 
		baum{tag_id:xxx, device_id:xxx GPS:xxx, date: xxx}
		in here column names of table are fixed. When table elements ist changed, this function must be changed too. 
		
	6) query_table(table_name)
		table_name : string
		read the table totally
		
	7) query_table_id(tag_id)
		tag_id : string
		read the table according to tag_id ordered by date
		
	8)query_table_ele(table_ele, target)
		table_ele, target : string
		read the table according to "table_ele" and its target ordered by date
		e.g. : query_table_ele('device_id', 'ID23451')
		
	9) delete_table_id(tag_id)
		tag_id : string
		delete the rows which tag_id is tag_id hier
		
	12) gps_map_marker(baums)
		GPS location mark on map
 		Connect points in time order
		baums: list from query
		
		

    Additional  for login.
	Precondition : administer right, create user_role: Role_r and Role_rw 
				   see initial_role.sql
	
	10) create_login_r(username, password)
		username, password : string
		create a only read login_name and password 
		
	11) create_login_rw(username, password)
		username, password : string
		create a write read login_name and password		
		
		
4. program in the Raspberry Pi 


    1) the connecting information were changed. They are in Class direct define and fixed. 
        in Class: see method "get_connect". 
        funktion: function "main()" were changed and simplify.  Called directly.
    2) program Modul "funktion" in Ras[berry Pi is not updated. That means the default_table cloud not be changed in one step.
    3) therefore, wenn you want to run the program in Pi, you'd better create a table named baum_test.
        
    
