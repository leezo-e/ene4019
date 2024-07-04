#필요한  패키지지와 모듈을 불러온다 

import sys, socket, time, os
from io import BytesIO
from urllib.parse import parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

# 우리는 단일 스레딩이 아닌 멀티스레딩을 사용하므로, 
# ThreadingBaseServer classsms threadingMinIn과 HTTPServer를 상속하게 한다

class ThreadingBaseServer(ThreadingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)

# MyHTTP zmffotmsms import 해왔던 BaseHTTPRequestHandler를 상속한다
# def do_GET은 HTTP GET 요청을 처리하는 데에 사용된다

class MyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if 'HTTP/1.0' in self.request_version:
                #HTTP/1.0 프로토콜 버전은 400 bad request로 처리한다. 
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'400 Bad Request')
                
            # 요청 경로가 '/'인 경우, 'index.html 파일을 읽어와 200 OK 응답을 한다. 
            # Content-length 헤더를 1024로 설정해서 HTML 컨텐츠를 입력한다.
            if self.path == '/index.html':
                with open('index.html', 'rb') as file:
                    content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)

            
            # 요청 경로가 /image.jpg 인 경우에는 해당 명의 파일을 읽어와 200 OK를 응답하고, 
            # content-length를 1024로 설정하여 이미지 컨텐츠를 응답한다.
            elif self.path == '/image.jpg':
                # 이미지 요청을 처리
                with open('image.jpg', 'rb') as image:
                    content = image.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-Length', 1024)  # Content-Length 헤더 설정
                    self.end_headers()
                    self.wfile.write(content)

    
        except FileNotFoundError: #만약에 파일을 찾지 못한다면 404 not found를 반환하게 한다 
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        try:
            # Content-Length 헤더를 이용하여 요청 바디의 크기를 가져옵니다.
            content_length = int(self.headers['Content-Length'])
            # 요청 바디를 읽어옵니다.
            body = self.rfile.read(content_length)
            
            # POST 데이터를 디코딩합니다.
            post_data = body.decode('utf-8')
            
            # 요청 경로가 '/test/picResult'인 경우 POST 데이터를 출력합니다.
            if self.path == '/index.html':

                # 응답을 보냅니다.
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response = f"POST data received successfully: {post_data}"
                self.wfile.write(response.encode('utf-8'))

        except Exception as e:
            # 예외가 발생하면 500 Internal Server Error를 응답합니다.
            print('Error processing POST request:', str(e))
            self.send_error(500)

# 웹 서버를 포트 8000에서 시작하고 이를 계속 실행하도록 설정한다.
# 서버가 시작됨을 보이는 메시지와 종료 방법을 출력했다.

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 9898), MyHTTP)
    print('Started WebServer')
    print('Press Ctrl + c to quit webserver')
    server.serve_forever()