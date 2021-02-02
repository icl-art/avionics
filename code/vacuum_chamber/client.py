"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from typing import List, Tuple
import pandas as pd

pressures = []
temperatures = []
class S(BaseHTTPRequestHandler):
    

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global pressures
        global temperatures
        self._set_response()
        self.wfile.write(str.encode(self.data_to_tables(pressures, temperatures)))

    def data_to_tables(self, pressures: List[Tuple[float, float]], temperatures: List[Tuple[float, float]]):
        string = "<html><meta http-equiv=\"refresh\" content=\"0.5\"/>"
        string += self.make_table(pressures, ["Time", "Pressure"])
        string += self.make_table(temperatures, ["Time", "Temperature"])
        return string + "</html>"

    def make_table(self, values, headers):
        string = "<table>"
        encode_tuple = lambda k, v: f"<tr><td>{k}</td><td>{v}</td></tr>"
        string += encode_tuple(*headers)
        for k, v in values:
            string += encode_tuple(k, v)
        return string + "</table>"

    def do_POST(self):
        global pressures
        global temperatures
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode("utf-8") # <--- Gets the data itself
        data = {k:float(v) for k, v in map(lambda kv: kv.split("="), post_data.split("&"))}
        try:
            t = time.time()
            pressures += [(t, data["pressure"])]
            temperatures += [(t, data["temperature"])]
        except:
            print("Exception occured")
            print(data)
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    df = pd.DataFrame(pressures)
    df.to_csv("pressures.csv", header=["Time", "Pressure"], index=False)
    df = pd.DataFrame(temperatures)
    df.to_csv("temperatures.csv", header=["Time", "Temperature"], index=False)
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()