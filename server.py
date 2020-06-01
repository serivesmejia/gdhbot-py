from flask import Flask
from threading import Thread

class GDHKeepAliveServer:
    app = Flask('')

    @app.route('/')
    def index():
      return "Bot alive, yay!<p>~M.M</p>"

    def start(self):
      self.app.run(host="0.0.0.0", port=8080)

    def asyncStart(self):
      server = Thread(target=self.start)
      server.start()