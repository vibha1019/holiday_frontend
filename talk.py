import sys

class frontend:
    def __init__(self):
        pass
    def send(self,data,path):
        with open(path, 'w') as file:
            file.write(data)
    def fetch(self):
        with open("/socialmedia_backend_fork/talk.py", 'r') as file:
            return file.read()
