from os import path
from fabric import Connection

def find_file(file_path):
	
	if path.exists(file_path):
		return True
	return False

def get_file_status(_conn, file_path):
	
	_res = _conn.run('cat %s | grep "Status:"'%file_path)
	if 'S (sleeping)' in _res:
		return False
	elif '' in_res:
		return True

if __name__ == "__main__":

	hosts = { "10.20.12.08": {'Username': 'admin', 'Password': 'p@ssW0rd'},
		      "10.20.12.12": {'Username': 'admin', 'Password': 'p@ssW0rd'},
			  "10.20.12.21": {'Username': 'admin', 'Password': 'p@ssW0rd'},
			  "10.20.12.22": {'Username': 'admin', 'Password': 'p@ssW0rd'} }

	file_path = "/proc/21"
	print(find_file(file_path))
	
	for host, data in hosts.items():
		_conn = Connection(host=host, user=data['Username'], connect_kwargs={"password": data['Password']})
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
