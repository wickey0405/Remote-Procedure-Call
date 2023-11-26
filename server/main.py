from Server import Server
from Calculator import Calculator

port = 3000
server = Server('localhost', port)
calculator = Calculator()

server.createServer()

while True:
    connection_prop = server.connectClient()

    try:
        while True:
            try:
                json_data = server.recieveData(connection_prop, True)             
                calculator.setInfo(json_data)
                result= calculator.runFunc(json_data)
                server.createResponseJSON(result, connection_prop, True)

            except:
                print('no data from', connection_prop['client_address'])
                break
    finally:
        print('Closing connection')
        connection_prop['connection'].close()