from flask import Flask,request,render_template,redirect
import json
import os
from Helpers.Helpers import getResp,run_docker

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/submit",methods = ["POST"])
def create_yaml():
    data = {
        'project_name':request.form['projectName'],
        'project_folder_path': request.form['folderName'],
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


@app.route("/handle-deployment",methods=["POST"])
def handler():
    with open("project_details.json", 'r') as file:
        data = json.load(file)
    project_folder = data['project_folder_path']
    os.chdir(path=project_folder)
    query = f"Generate a Dockerfile for the following project details: Framework: {data['framework_name']}, Version: {data['framework_version']}, Port Number: {data['port_number']}, Description: {data['description']}, Environment: {data['environment']}. The Dockerfile should be created based on these details. Also, use the ubuntu:latest as the base image and make installations on top of it. Also, dont generate anything else except for the docker file content. DO NOT GENERATE ANY HEADER OR FOOTER"
    docker_resp = getResp(query)

    with open('dockerfile','w') as file:
        file.write(docker_resp)
    project_name = data["project_name"]
    port = data['port_number']
    id,ip = run_docker(project_folder,project_name,port)

    return render_template('success.html', container_ip=ip, container_id=id)  

if __name__=="__main__":
    app.run()
