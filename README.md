# ATP

1.Precondition

	1)modul psmssql in python installed
	
	2)SQL Server: host, username, password, database

	
2.Funktion

	1) main(server host, username, password, database)
		connect to the SQL Server and database
		return a connect
	
	2) creat_table(table_name)
		table_name : string
		create a table which include tag_id, device_id, GPS, date
	
	3) drop_table(table_name)
		table_name : string
		drop a table totally
		
	4) insert_table_batch(baum_list,table_name='baum_test')
		insert batch information to the table 
		baum_list : list
		defaul table : baum_test
		list[{baum1}, {buam2},...], element of the list is a dictionary. Its key correspond to the column of the table
		
	5) insert_table(baum)
		insert single information to the table
		baum : dictionary, correspond to the table 
		baum{tag_id:xxx, device_id:xxx GPS:xxx, date: xxx}
		
	6) query_table(table_name)
		table_name : string
		read the table totally
		
	7) query_table_id(tag_id)
		tag_id : string
		read the table according to tag_id ordered by date

	8)query_table_ele(table_ele, target)
		table_ele, target : string
		read the table according to "table_ele" and its target ordered by date
		e.g. : query_table_ele('device_id', 'rgs23451')
		
	9) delete_table_id(tag_id)
		tag_id : string
		delete the rows which tag_id is tag_id hier
		
		
	Precondition : administer right, create user_role: Role_r and Role_rw 
				   see initial_role.sql
	
	10) create_login_r(username, password)
		username, password : string
		create a only read login_name and password 
		
	11) create_login_rw(username, password)
		username, password : string
		create a write read login_name and password		
		
	
