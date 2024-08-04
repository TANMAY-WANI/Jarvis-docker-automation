from flask import Flask,request,render_template,redirect
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/submit",methods = ["POST"])
def create_yaml():
    data = {
        'project_folder': request.form['folderName'],
        'framework_name': request.form['frameworkName'],
        'framework_version': request.form['frameworkVersion'],
        'port_number': request.form['portNumber'],
        'description': request.form['description'],
        'environment': request.form['environment']
    }
    with open('project_details.json', 'w') as file:
        json.dump(data, file, indent=4)

    return redirect("/deploy")

@app.route("/deploy")
def display_deployment_page():
    return render_template("deploy.html")


if __name__=="__main__":
    app.run()
