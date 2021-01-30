from os import path
from fabric import Connection


def deploy(_conn):
	
	stop_webserver(_conn)
	update_repository(_conn)
	start_webserver(_conn)
	
	
def stop_webserver(_conn):
	res = _conn.run('systemctl stop nginx')
	
	
def update_repository(_conn, repo_path) :
	
	res = _conn.run("cd %s"%srepo_path)
	res = _conn.run("git pull")

def start_webserver(_conn):

	res = _conn.run("systemctl start nginx")


if __name__  == "__main__":
	
	host = {'host':'10.20.12.45', 'Username:':'admin', 'Password':'p@ssW0rd'}
	
	_conn = Connection(host=host['host'], user=host['Username'], connect_kwargs={"password": host['Password']})
	
	deploy(_conn)
	
	
	
	
	
	
	
	
	
	
