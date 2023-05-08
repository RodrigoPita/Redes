import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5005        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect( ( HOST, PORTA ) ) 

print( f'\nT R A D U T O R - D E - R E D E S\n\n'+
      f'Digite uma das palavras a seguir para descobrir sua tradução em inglês:\n'+
      f'- rede - enlace - link - roteador -\n'+
      f'- comutador - cliente - servidor - hospedeiro -\n'+
      f'- navegador - endereço IP - fim-a-fim -\n'  )
while True:
    # define a string para envio da mensagem ou codigo de parada
    aux = input( 'Digite a palavra: ' )

    # codigo de parada
    if aux == 'stop': break
    
    # envia uma mensagem para o par conectado
    sock.send(bytes(aux, 'utf-8'))
    
    #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
    msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem

    # imprime a mensagem recebida
    print(str(msg,  encoding='utf-8'))

# encerra a conexao
sock.close()
