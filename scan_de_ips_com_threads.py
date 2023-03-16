import ipaddress
import socket
import concurrent.futures
from timeit import default_timer as timer

# Range de IPs
network = ipaddress.ip_network('192.168.15.0/24')
portas = [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 445]


def scan(ip):
    for porta in portas:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.1)
        codigo = cliente.connect_ex((str(ip), porta))

        if codigo == 0:
            try:
                output = socket.gethostbyaddr(str(ip))
                hostname = str(output).split("'")[1::2][0]
            except:
                hostname = 'Sem hostname'
            print(f'Testando: {ip}:{porta} -> Aberta | {hostname}')


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for subrede in network.subnets(prefixlen_diff=2):
            for ip in subrede:
                executor.submit(scan, ip)
    print('Scan Finalizado!')


if __name__ == '__main__':
    start = timer()
    main()
    tempo = timer()-start
    print(f'Tempo: {tempo:.2f} segundos')
