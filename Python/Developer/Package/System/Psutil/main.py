import psutil

# Get CPU usage percentage
print(psutil.cpu_percent(interval=1))  # 1-second interval

# Get number of logical and physical cores
print(psutil.cpu_count(logical=True))   # Logical cores
print(psutil.cpu_count(logical=False))  # Physical cores

# Get RAM usage
memory_info = psutil.virtual_memory()
print(memory_info.total)    # Total RAM
print(memory_info.available)  # Available RAM
print(memory_info.percent)  # Percentage used

# Get disk usage statistics
disk_info = psutil.disk_usage('/')
print(disk_info.total)     # Total space
print(disk_info.used)      # Used space
print(disk_info.free)      # Free space
print(disk_info.percent)   # Percentage used

# Get disk partitions
print(psutil.disk_partitions())

# Get network stats
network_info = psutil.net_io_counters()
print(network_info.bytes_sent)  # Total bytes sent
print(network_info.bytes_recv)  # Total bytes received

# Get network interfaces
print(psutil.net_if_addrs())

# Get all running processes
for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    print(process.info)

# Get a specific process by PID
process = psutil.Process(3548)  # Replace 1234 with a PID
print(process.name())           # Process name
print(process.status())         # Process status
print(process.cpu_percent())    # CPU usage
print(process.memory_info().rss)  # RAM usage in bytes

# Kill a process
process.terminate()

battery = psutil.sensors_battery()
if battery:
    print(f"Battery percentage: {battery.percent}%")
    print(f"Power plugged in: {battery.power_plugged}")
