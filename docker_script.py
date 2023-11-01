#!/usr/bin/python3


import os
# check if Docker is already installedimport subprocess

def install_docker():
    try:
        # Check if Docker is already installed
        check_installed = subprocess.run(["docker", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check_installed.returncode == 0:
            print("Docker is already installed.")
            return

        # Install Docker (for Ubuntu)
        install_command = "sudo apt-get update && sudo apt-get install -y docker.io"
        subprocess.run(install_command, shell=True, check=True)

        # Start and enable the Docker service
        subprocess.run(["sudo", "systemctl", "start", "docker"])
        subprocess.run(["sudo", "systemctl", "enable", "docker"])

        print("Docker installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error installing Docker: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    install_docker()


