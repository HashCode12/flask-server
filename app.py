from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

def get_server_ip():
    """Attempt to get the local machine’s primary IP address."""
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = 'Unavailable'
    return ip

@app.route("/")
def index():
    # Remote address seen by Flask
    client_ip = request.remote_addr

    # X-Forwarded-For header (could be a comma-separated list)
    forwarded = request.headers.get('X-Forwarded-For', '')

    return jsonify({
        "client_ip": client_ip,
        "forwarded_for": [ip.strip() for ip in forwarded.split(',')] if forwarded else [],
        "server_ip": get_server_ip()
    })

    print("Hello")
    print("Hello")


if __name__ == "__main__":
    # Use 0.0.0.0 so it’s reachable from outside the container/host
    app.run(host="0.0.0.0", port=5000)
