import subprocess
from subprocess import Popen, PIPE

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

process = Popen(["grep", "search_term"], stdin=PIPE, stdout=PIPE, text=True)
output, error = process.communicate(input="example input text")
print(output)

output = subprocess.check_output(["echo", "Hello, World!"], text=True)
print(output)

exit_code = subprocess.call(["ls", "-l"])
print("Exit Code:", exit_code)

subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
