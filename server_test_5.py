from flask import Flask,render_template
server_test_5_app = Flask(__name__,template_folder='D:/PythonProgram/backend_test5/template_folder/')

@server_test_5_app.route('/')
def get_request():
    return render_template('server_test_5.html')

if __name__ == "__main__":
    server_test_5_app.run(debug=True)