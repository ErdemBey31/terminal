import subprocess
from flask import Flask, render_template, request
from subprocess import PIPE, STDOUT

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    user_command = request.form['command']
    result = run_command(user_command)
    return result

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        output = ''
        while True:
            line = process.stdout.readline()
            if not line:
                break
            output += line
        return output
    except subprocess.CalledProcessError as e:
        return "ERROR: " + str(e.output)
