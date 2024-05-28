import os
import time
import psutil
import configparser

# 설정 파일 읽기
config = configparser.ConfigParser()
config.read('config.ini')

program_path = config.get('Settings', 'program_path')
program_options = config.get('Settings', 'program_options')

def is_program_running(program_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == program_name:
            return True
    return False

def start_program():
    command = f'"{program_path}" {program_options}'
    os.system(command)

if __name__ == "__main__":
    program_name = os.path.basename(program_path)
    while True:
        if not is_program_running(program_name):
            start_program()
        time.sleep(5)  # Check every 5 seconds