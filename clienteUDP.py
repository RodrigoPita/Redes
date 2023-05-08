import socket

UDP_IP = "127.0.0.1" # endereço IP local
UDP_PORT = 5005      # porta que o servidor está escutando

print( f'\nT R A D U T O R - D E - R E D E S\n\n'+
      f'Digite uma das palavras a seguir para descobrir sua tradução em inglês:\n'+
      f'- rede - enlace - link - roteador -\n'+
      f'- comutador - cliente - servidor - hospedeiro -\n'+
      f'- navegador - endereço IP - fim-a-fim -\n' )

while True:
    message = input("Digite a palavra: ")
    if message.lower() == 'exit': break# se a mensagem for 'exit', termina a conexão
    message_bytes = message.encode('utf-8') # converte a mensagem para bytes
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(message_bytes, (UDP_IP, UDP_PORT)) # envia a mensagem para o servidor
    data, server_addr = sock.recvfrom(1024) # espera pela mensagem de resposta

		# imprime a mensagem de resposta
    print("Mensagem do servidor {}: {}".format(server_addr, data.decode('utf-8')))
    sock.close() # fecha o socket
