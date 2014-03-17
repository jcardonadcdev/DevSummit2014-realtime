import os, sys
import time, argparse
import socket

def sendData(sock, dataPath, interval):
    dataFile = None
    i = 0
    
    try:
        interval = float(interval / 1000.0)
        
        if not os.path.exists(dataPath):
            raise Exception("Data file not found: %s." % dataPath)
        
        #open simulation data file and send data
        dataFile = open(dataPath, "r")
        print "Opened data file: %s" % dataPath
        for l in dataFile:
            sock.send(l)
            time.sleep(interval)
        dataFile.close()
        dataFile = None
        return True
        
    except Exception as e:
        raise Exception("Error sending data: %s" % e)
    finally:
        if dataFile:
            dataFile.close()
        
    
#make argument parser to handle user command line input
parser = argparse.ArgumentParser(description="Start a simulated data feed for a GeoEvent Processor tcp text input")
parser.add_argument("-d", "--data", help="path to file containing csv data. Default is ../data/WorkerSimulation.csv", default="../data/WorkerSimulation.csv")
parser.add_argument("-p", "--port", help="tcp socket port. Default is 5565", type=int, default=5565)
parser.add_argument("-n", "--name", help="host name of server to connect to. Default is 'localhost'", default="localhost")
parser.add_argument("-i", "--interval", help="interval in milliseconds between messages. Default is 100. Maximum interval is 5 seconds", type=int, default=100)
parser.add_argument("-l", "--loop", help="flag to run continous loop. Default is False", type=bool, default=False)
parser.add_argument("-s", "--skip", help="flag to skip first line of data. Default is True", type=bool, default=True)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.interval > 5000:
        print "Warning: interval cannot be more than 5 seconds. Setting interval to 5 seconds"
        args.interval = 5000
    if args.interval < 0:
        print "Warning: Invalid interval value. Setting interval to default value"
        args.interval = 1000    
    
    #begin simulation
    tcpSocket = None
    cont = True
    try:
        #Check if data file exists
        if not os.path.exists(args.data):
            raise Exception("Data file not found: %s." % args.data)
        
        #open socket
        tcpSocket = socket.create_connection((args.name, args.port))
        print "Opened tcp socket on %(name)s:%(port)s" % {"name": args.name, "port": args.port}
        
        while cont:
            sendData(tcpSocket, args.data, args.interval)
            cont = args.loop
        
        print "Done"
        
    except Exception as e:
        print "Error: %s" % e
    finally:
        if tcpSocket:
            tcpSocket.close()