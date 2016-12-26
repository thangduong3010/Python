import os
import time

# 1. The files and directories to be backed up are
# specified in a list
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Unix\Linux
# source = ['/home/python/notes']
source = ["F:\\Github\\Python\\Practice\\Files\\data", "F:\\Github\\Python\\Practice\\Files\\log", "F:\\demo\\log"]


# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Unix\Linux
# target_dir = '/home/python/backup'
target_dir = "F:\\Github\\Python\\Practice\\Files\\backup"

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3. The files are backed up into a zip file
# 4. The current day is the name of the subdirectory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip file
now = time.strftime('%H%M%S')

# Take comment from user to
# create the name of the zip file
comment = raw_input("Enter a comment --> ")

# Check if a comment was entered
# The name of the zip file
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print("!Successfully created directory {}".format(today))

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,' '.join(source))

# Run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to {}".format(target))
else:
    print("Backup failed")