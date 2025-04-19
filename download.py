import paramiko

# Define SSH server details
host = "test.rebex.net"  # Public SSH test server
port = 22
username = "demo"
password = "password"
remote_file_path = "newfile.txt"  # File created earlier
local_file_path = "downloaded_newfile.txt"  # File to save locally

try:
    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    client.connect(host, port, username, password)
    print(f"Connected to {host}")

    # Open an SFTP session
    sftp = client.open_sftp()

    # Download the file
    sftp.get(remote_file_path, local_file_path)
    print(f"File downloaded successfully as '{local_file_path}'")

    # Close SFTP and SSH sessions
    sftp.close()

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()
    print("SSH connection closed.")
