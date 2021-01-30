from os import path
from fabric import Connection



def deploy(_conn):


	run_container(_conn)
	
	
def run_container(_conn):
	
	# pull docker image	
	docker_regi_path = "registry.webuy.com:5000/mywebserver"
	res = _conn.run('docker pull %s'%docker_regi_path)
	
	# run docker image
	_image_name = "mywebserver"
	res = _conn.run("docker run -dit -p 127.0.0.1:80:5000 --name %s "%_image_name )
	
	
	

if __name__ == "__main__":

	hosts = { "10.20.12.08": {'Username': 'admin', 'Password': 'p@ssW0rd'},
		      "10.20.12.12": {'Username': 'admin', 'Password': 'p@ssW0rd'} }
	
	# Deploy container on AWS instances.
	for host, data in hosts.items():	
		_conn = Connection(host=host, user=data['Username'], connect_kwargs={"password": data['Password']})
	
		deploy(_conn)

	# create a cloud formation template. 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
