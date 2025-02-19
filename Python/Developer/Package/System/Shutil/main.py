import shutil

shutil.copy('file.txt', 'backup.txt')
shutil.copytree('source_folder', 'destination_folder')
shutil.move('file.txt', 'new_folder/file.txt')
shutil.rmtree('old_folder')

usage = shutil.disk_usage('/')
print(f'Total: {usage.total}, Used: {usage.used}, Free: {usage.free}')
