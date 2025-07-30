import subprocess
import platform
import csv
import datetime


def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def load_hosts():
    """
    Эта функция должна читать IP-адреса из файла 'hosts.csv',
    обрабатывать каждую строку и возвращать список IP-адресов.
    """
    ip_list = []
    
    with open("hosts.csv", "r") as file:
        for line in file:
            cleaned_string = line.strip()
            ip_list.append(cleaned_string)
            
    return ip_list
    

def log_result(ip, status):
    """
    Эта функция должна записывать результат пинга (IP, статус, время) в файл 'log.csv'.
    """

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, ip, status])


def main():
    hosts_to_ping = load_hosts() # функция load_hosts() будет вызвана здесь

    for ip in hosts_to_ping:
        is_online = ping(ip)
        status_text = "Online" if is_online else "Offline"
        print(f"{ip}: {status_text}")
        
        log_result(ip, status_text)

if __name__ == "__main__":
    main()
