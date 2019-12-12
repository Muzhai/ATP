
EXEC sp_addrole 'Role_rw'						-- create a user role
GRANT SELECT,INSERT ON baum_test TO Role_rw		--give the role select and insert right to table baum_test

---------------------------------------------------------------------------------------------
EXEC sp_addrole 'Role_r'						--create a user role
GRANT SELECT ON baum_test TO Role_r				--give the role only_read right to table baum_test


EXEC sp_addlogin 'halloworld','123456','Baum'	--create a login name and passerword to login SQL Server for database Baum
create user halloworld for login halloworld with default_schema=Role_rw  --create a user "halloworld" of the database and mapping to login_name "halloworld" in Role_rw
EXEC sp_addrolemember 'Role_rw','halloworld'	-- add user name 'halloworld' to role 'Role_rw'
----------------------------------------------------------------------------------------------
--exec sp_change_users_login 'Update_One', 'user_rw', 'newlogin'  --更改用户名和登录名的对应的映射关系







