#!/home/pydev/mobileApp/.venv/bin/python3

import os
import socket
import dotenv

homeDir = os.path.expanduser('~')
envFile = os.path.join(f"{homeDir}/mobileApp/.env")
dotenv.load_dotenv(envFile)

BUFFER_SIZE = 1200
IP, PORT = os.getenv('host'), int(os.getenv('port'))

UPLOAD_DIRECTORY = './uploads'

FLCT_START =    b'<<__START__>>'
FLCT_FILENAME = b'<<__FILENAME__>>'
FLCT_FILESIZE = b'<<__FILESIZE__>>'
FLCT_BYTES =    b'<<__BYTES__>>'
FLCT_FINISHED = b'<<__FINISHED__>>'
FLCT_END =      b'<<__END__>>'
FLCT_OK =       b'<<__OK__>>'


def _read_message(conn) -> bytes:
    buffer = b''

    while True:
        data = conn.recv(BUFFER_SIZE)
        buffer += data

        if buffer.startswith(FLCT_START) and buffer.endswith(FLCT_END):
            break
        
        if buffer == FLCT_OK:
            break

    return buffer


def client_mode(server_addr: str, server_port: int, absolute_path: str):
    server_sock_data = server_addr, server_port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_sock_data)

    filename = os.path.basename(absolute_path)
    filesize = os.stat(absolute_path).st_size
    print('INFO file {}, size {} bytes.'.format(filename, filesize))

    message = FLCT_START + FLCT_FILENAME + filename.encode() + FLCT_END
    sock.sendall(message)
    data = _read_message(sock)
    if data != FLCT_OK:
        print('ERROR abort.')

    message = FLCT_START + FLCT_FILESIZE + str(filesize).encode() + FLCT_END
    sock.sendall(message)
    data = _read_message(sock)
    if data != FLCT_OK:
        print('ERROR abort.')
    
    sending_bytes = 0
    percentage_step = 10

    fd = open(absolute_path, 'rb')
    while True:
        chunk = fd.read(BUFFER_SIZE)
        if chunk:
            sock.sendall(FLCT_START + FLCT_BYTES + chunk + FLCT_END)
            data = _read_message(sock)
            if data != FLCT_OK:
                print('ERROR abort.')
            
            sending_bytes += len(chunk)
            percentage = 100 * sending_bytes / filesize
            
            if percentage >= percentage_step:
                print('INFO sending {}%'.format(percentage_step), end='\r')
                percentage_step += 10
        
        else:
            break
    
    print('INFO sending 100%')
    
    sock.sendall(FLCT_START + FLCT_FINISHED + FLCT_END)
    data = _read_message(sock)
    if data != FLCT_OK:
        print('ERROR abort.')
    
    print('INFO file {} sended.'.format(filename))
    sock.close()

if __name__=='__main__':
    myDir = '/home/pydev/Documents/cjour'
    elements = os.listdir(myDir)
    for element in elements:
        path = os.path.join(myDir, element)
        if os.path.isfile(path):
            client_mode(IP, PORT, path)
        else:
            print('not file !')


