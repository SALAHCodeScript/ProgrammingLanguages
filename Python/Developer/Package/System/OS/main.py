import os

path = "D:\\Data\\SALAH\\Linux\\home\\salah"

working_directory = os.getcwd()
os.chdir(path)
list_items = os.listdir()

os.mkdir("new_folder")
os.makedirs("nested/folder/structure")
os.remove("file.txt")
os.rmdir("empty_folder")
os.rename("old_name.txt", "new_name.txt")

environment_variable = os.environ["PATH"]
safty_environment_variable = os.getenv("PATH", "/default/path")

os.path.join(path, "Documents")
os.path.exists(path)
os.path.isdir(path)
os.path.isfile(path)
full_path = os.path.abspath(path)

os.system('echo "Hello World"')
pid = os.getpid()

symbol_path = os.sep
os_name = os.name
random_bytes = os.urandom(8)

fd = os.open("file.txt", os.O_RDWR | os.O_CREAT)
load_file = os.read(fd)
os.write(fd, b"Hello, World")
os.close(fd)
