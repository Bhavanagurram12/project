from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/run_python_script")
def run_python_script():
    result = subprocess.check_output(["python", "run_python_script.py"]).decode("utf-8")
    return result

if __name__ == "__main__":
    app.run(debug=True)