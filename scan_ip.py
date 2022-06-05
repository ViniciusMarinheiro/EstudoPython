import socket

# Colocar IP de acordo com o range de IP da rede (alterar apenas o valor 15 caso necessário)
ip = '192.168.15.'
portas = [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 445]

def scan():

# Incrimenta o final do IP de 0 a 255
    final_ip = list(range(256))
    for final in final_ip:
        ip_certo = f'{ip}{final}'
        
        for porta in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(0.1)
            codigo = cliente.connect_ex((ip_certo, porta))
            
# Printa IPs com portas da lista abertas
            if codigo == 0:
                print(f'Testando: {ip_certo}:{porta} -> Aberta')
    print('Scan Finalizado!')

scan()
