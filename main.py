import paramiko

# Define SSH server details
host = "test.rebex.net"  # Public SSH test server
port = 22
username = "demo"
password = "password"

try:
    # Create an SSH client
    client = paramiko.SSHClient()

    # Automatically add the server key if missing
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    client.connect(host, port, username, password)
    print(f"Connected to {host}")

    # Command to create a new file on the remote server
    command = "touch newfile.txt"
    stdin, stdout, stderr = client.exec_command(command)

    # Print command output (if any)
    print(stdout.read().decode())
    print(stderr.read().decode())

    print("File 'newfile.txt' created successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    client.close()
    print("SSH connection closed.")
