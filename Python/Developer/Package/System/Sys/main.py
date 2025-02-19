import sys

print(sys.argv)

sys.stdout.write("Hello, world!\n")
sys.stderr.write("This is an error!\n")

print(sys.path)
print(sys.platform)
print(sys.version)

sys.setrecursionlimit(2000)

x = [1, 2, 3]
print(sys.getsizeof(x))

sys.exit("Exiting the program")
