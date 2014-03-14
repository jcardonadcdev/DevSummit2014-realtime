DevSummit2014-realtime
======================

Demos Shown at the 2014 Esri Developer Summit tech session - Building Real-time web apps with GEP and JS API. The Worker Tracking application uses services hosted on ArcGIS Online.
To avoid data conflicts, the Worker Tracking application does not write data to a Feature Service as was mentioned in the tech session. Instead, the data has been staged to a Feature Service.
More information on GeoEvent Processor can be found at http://pro.arcgis.com/share/geoevent-processor/. This page has links to conceptual documents, help documents, and tutorials.

## Requirements
- ArcGIS GeoEvent Processor for Server
- The GeoEvent Simulator application
- Browser that supports web sockets. Check by going to http://www.websocket.org/ or by looking for the browser version at http://caniuse.com/websockets.

## Setup
- Either fork this repository or download it.
- Configure GeoEvent Processor
    - Open GeoEvent Processor Manager application (https://geoeventprocessor_host:6143/geoevent/manager).
    - Go to the "Site" tab and click on "Configuration Store" on the left panel.
    - Click "Import Configuration" to open up an import dialog.
    - Click the "Choss file" button and select the "data/GeoEventConfig.xml" file.
    - This should import:
        - A GeoEvent Definition named "FieldWorker"
        - A GeoEvent Service named "worker-incident-service"
        - An input named "worker-text-in"
        - An output named "incident-fjson-ws-out" and an output named "worker-fjson-ws-out"
- Copy web applications to a web server. This includes the two html files, "simplewebsocket.html" and "WorkerTrackingFullDemo.html", the "images" directory and the "css" directory.
    -NOTE: The directory must be accessible by url, so it must be in a virtual directory. If you do not have access to a web server, you can copy the files to GeoEvent Processor's "assets" directory and access the web pages by using http://host:6180/geoevent/assets.

## Running the simulator
- Open the GeoEvent Simulator application
- Browse to the file "data\WorkerSimulation.csv"
- Click the Checkbox labeled "Skip the First" to skip the first line
- Set the time field to be the 3rd field
- Click "Load"
- Set the message rate to be 1 message per 100 ms
- Click the play button to start the simulation
- Check the GeoEvent Processor Manager's Monitor tab to make sure data is flowing through the system

## Using the websites

### simplewebsocket.html

This is a sample web application that shows how to connect to a Web Socket endpoint of GeoEvent Processor and display messages in a text area. In a browser that supports web sockets, go to http://host:port/directory_name/simplewebsockets.html.

- In the textbox labeled "Websocket url" enter the url to the "worker-fjson-ws-out" output's url path. It is http://geoevent_processor_host:6180/workerlocations.
- Click the "ConnectWS" button and the textbox should turn green and a message should show in the "Messages Received" text area saying "Opened Web Socket".
- If the simulator is started, messages should start appearing.
- Click  "DisconnectWS" button to close the connection.

## WorkerTrackingFullDemo.html

This is a sample web application that uses the ArcGIS JavaScript API's StreamLayer to display real-time locations of field workers and alerts when a worker enters or exits an area of interest. In a browser that supports web sockets, go to http://host:port/directory_name/WorkerTrackingFullDemo.html
When the applcation opens, the "Workers" and "Incidents" text on the left panel should turn green to show that web socket connections have been made.
If the simulator is started, points should appear on the map and labels for each worker should appear on the left panel.

- Click on the "Identify Worker" button to show a halo around the worker's location point.
- When an incident is detected (a worker has entered/exited one of the red areas) you can click on the "Show History" button to show the locations where the worker has traveled.

## Coming soon

A python script that feeds simulated data to GeoEvent Processor so people on non-Windows machines can simulate the data feed.
