'''tcp 使用 select 模块'''
import select
import socket
import sys
import queue

#Create a tcp/ip socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)

#Bind the socket to the port
server_address = ('localhost',10000)
print('starting up on {} port {}'.format(*server_address),file=sys.stderr)
server.bind(server_address)

#Listen for incoming connection
server.listen(5)

#Socket from which we expect to read
inputs = [server]

#Socket to which we expect to write
outputs = []

#Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:
    #Wait for at least one of the socket to be ready for processing
    print('waiting for the next event',file=sys.stderr)
    readable,writable,exceptional = select.select(inputs,outputs,inputs)
    #Handle inputs
    for s in readable:
        if s is server:
            #A "readable" socket is ready to accept a connection
            connection,client_address = s.accept()
            print('connection from',client_address,file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            #Give the connction a queue for data we want to send
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print('received {!r} from '.format(data),file=sys.stderr)
                message_queues[s].put(data)
                #Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                #interpret empty result as closed connection
                print('closing',client_address,file=sys.stderr)
                #stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                #Remove message queue
                del message_queues[s]
    #Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            #No messages wating,so stop checking for writability
            print(' ','queue empty',file=sys.stderr)
            outputs.remove(s)
        else:
            print('sending {!r} to '.format(next_msg),file=sys.stderr)
            s.send(next_msg)

    #Handle exceptional condition
    for s in exceptional:
        print('exception condition on ',file=sys.stderr)
        #stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        #Remove mwssage queue
        del message_queues[s]
