import posixpath

path = posixpath.join("/home/user", "documents", "file.txt")
full_path = posixpath.abspath(path)

directory_name = posixpath.dirname("/home/user/file.txt")
basename = posixpath.basename("/home/user/file.txt")

splited_path1 = posixpath.split("/home/user/file.txt")
splited_path2 = posixpath.splitext("/home/user/file.txt")

normalize_path = posixpath.normpath("/home/user/../documents/file.txt")
expand_user = posixpath.expanduser("~/documents/file.txt")

posixpath.isabs("/home/user/file.txt")
posixpath.exists("/home/user/file.txt")  
posixpath.isfile("/home/user/file.txt")
posixpath.isdir("/home/user")
