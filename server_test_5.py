from flask import Flask,render_template
import os

server_test_5_app = Flask(__name__,template_folder=os.path.dirname(os.path.realpath(__file__)))

@server_test_5_app.route('/')
def get_request():
    return render_template('server_test_5.html')

if __name__ == "__main__":
    server_test_5_app.run(debug=True)