# PingThing

**PingThing** is a simple tool to visualize where network requests are coming from. It's especially useful for checking if incoming network requests can reach your Docker container.

## How It Works

1. Host the tool using Docker.
2. Open the web interface in your browser at `http://<your-ip>:5000`.
3. From another machine, run a simple `curl` command:

   ```bash
   curl http://<your-ip>:5000/ping
   ```
4. The web interface will display the source IP address of the request, confirming that the request was received.

## Use Cases
- Test if containers can receive requests from external sources
- Debug Docker network configurations
- Verify reachability between hosts


## Docker usage
The tool is available from the docker hub:
```
docker pull maximaaldocker/pingthing:latest
```
You can use the docker-compose.yml file as a reference for deploying the tool.



## How its made
PingThing uses:
- A Flask backend serving a simple web interface.
- A WebSocket connection updating the web interface in real time.
When a request is received at `/ping`, the Flask app captures the client's IP address and headers, and then sends this data to the connected front-end via the WebSocket.
