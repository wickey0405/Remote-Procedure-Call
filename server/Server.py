import socket
import json

class Server:
    def __init__(self, address, port):
        self.sock = None
        self.address = address
        self.port = port
        self.requestID_list = {}


    def createServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def connectClient(self):
        connection, client_address = self.sock.accept()
        connection_prop = {'connection': connection, 'client_address': client_address}
        return connection_prop
    
    def byteDataToJSON(self, data):
        header, body = data.decode('utf-8').split('\r\n\r\n', 1)
        json_data = json.loads(body)
        return json_data
    
    def append_requestID_list(self, json_data, connection_prop):
        saveData = {
            "connection": connection_prop.get('connection'), 
            "client_address": connection_prop.get('client_address')
            }
        self.requestID_list[json_data.get('id')] = saveData

    def recieveData(self, connection_prop, doesPrint=True):
        connection = connection_prop.get('connection')
        json_data = self.byteDataToJSON(connection.recv(4096))
        if doesPrint:
            print("----------recieved data----------")
            print(json_data)
        self.append_requestID_list(json_data, connection_prop)
        return json_data
    
    def createResponseJSON(self, response, connection_prop, doesPrint=True):
        res_json = json.dumps(response)
        sendData = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(res_json)}\r\n\r\n{res_json}"
        connection_prop.get('connection').sendall(sendData.encode('utf-8'))
        if doesPrint:
            print("----------send data-------------")
            print(response)
            print("----------completed-------------")
            print("")
