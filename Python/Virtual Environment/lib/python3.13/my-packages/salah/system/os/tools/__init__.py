import platform
import subprocess

def get_machine_name():
    return platform.system()

def get_output_command(command: list):
    cmd = subprocess.run(command, capture_output=True).stdout.decode()[:-1]
    return cmd

def get_error_command(command: list):
    cmd = subprocess.run(command, capture_output=True).stderr.decode()[:-1]
    return cmd

def get_environment_variable(env_var):
    environment_variable = get_output_command(["printenv"]).split('\n')
    for v in environment_variable:
        if v.startswith(f"{env_var.lower()}=") or v.startswith(f"{env_var.upper()}="):
            path = v[v.find('=')+1:]
    return path
