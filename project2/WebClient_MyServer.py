import http.client
import tkinter as tk
import io
from PIL import Image, ImageTk

host = 'localhost'
port = 9898 
connection = http.client.HTTPConnection(host, port)
user_agent = "2022001167/LEEZOE/WebClient/COMPUTERNETWORK"
header = {"User-Agent": user_agent}
    
class WebClient:
    def mission():
        # HTTP 요청 헤더에서 user-agent 확인하기 
        path = "/index.html"
        connection.request("GET", path)
        response = connection.getresponse()
        print("Response Message: %d %s" % (response.status, response.reason)) 

        print("Write your contents to send")
        contents = input()
        contents = contents.encode()
        path = "/index.html"
        connection.request("POST", path, contents)
        response = connection.getresponse()
        print("Response Message: %d %s" % (response.status, response.reason)) 
        print("Response Data: %s" % (response.read().decode()))
    

if __name__ == "__main__":
    web_client = WebClient()

    WebClient.mission()