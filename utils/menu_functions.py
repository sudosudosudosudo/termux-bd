import os
import subprocess
import time

def main_menu():
    print("Main Menu")
    print("1. Start Attack")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        pass  # Handle the start attack logic
    elif choice == "2":
        exit()

def read_duckyscript(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

def run(command):
    return subprocess.run(command, capture_output=True, text=True)

def restart_bluetooth_daemon():
    subprocess.run(['termux-bluetooth', 'stop'], check=True)
    time.sleep(1)
    subprocess.run(['termux-bluetooth', 'start'], check=True)
    time.sleep(1)

def get_target_address():
    return input("Enter the target Bluetooth address: ")
