from dotenv import load_dotenv
import os
import google.generativeai as genai
import subprocess
load_dotenv()
def getResp(query):
    api = os.getenv("GOOGLE_API")
    genai.configure(api_key=api)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(query)
    return response.text.replace("```","")


def run_docker(path,name,port):
    # os.chdir(path=path)
    img_name = "jarvis_image_"+name
    img_name = img_name.lower()
    build_command = [
        'docker','build','-t',img_name,'.'
    ]

    subprocess.run(build_command,check=True)

    container_name = "jarvis_container_"+name
    container_name = container_name.lower()
    run_cmd = [
        'docker','run','--name',container_name,'-d','-p',f"{port}:{port}",img_name
    ]
    result =subprocess.run(run_cmd,capture_output=True,check=True,text=True)
    container_id = result.stdout.strip()

    inspect_command = [
        'docker', 'inspect', 
        '--format', '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}', 
        container_id
    ]
    result =subprocess.run(run_cmd,capture_output=True,check=True,text=True)
    container_ip = result.stdout.strip()

    return container_id,container_ip




