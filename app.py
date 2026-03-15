import subprocess

def run_command(user_input):
    # Semgrep should flag this as command injection
    subprocess.call("ls " + user_input, shell=True)


password = "SuperSecretPassword123!"
