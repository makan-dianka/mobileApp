#!/home/pydev/mobileApp/.venv/bin/python3

import os
import socket
import sys
import dotenv

dotenv.load_dotenv('../.env')



BUFFER_SIZE = 1200
PORT = int(os.getenv('port'))

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


def server_mode(port: int):
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen()
    print('start server, listening on port {}.'.format(port))

    while True:
        conn, addr = sock.accept()
        print('connection accept, address {0[0]}:{0[1]}.'.format(addr))

        filename = ""
        filesize = 0
        fd = None
        
        received_bytes = 0
        percentage_step = 10

        try:
            while True:
                data = _read_message(conn)
                conn.sendall(FLCT_OK)
                
                data = data[len(FLCT_START):-len(FLCT_END)]
                
                if data.startswith(FLCT_FILENAME):
                    filename = data[len(FLCT_FILENAME):].decode()
                    print('INFO open file {}.'.format(filename))
                    fd = open(os.path.join(UPLOAD_DIRECTORY, filename), 'wb')
                    continue

                if data.startswith(FLCT_FILESIZE):
                    filesize = int(data[len(FLCT_FILESIZE):].decode())
                    print('INFO file size {} bytes.'.format(filesize))
                    continue

                if data.startswith(FLCT_BYTES):
                    if fd is None:
                        print('ERROR cannot open filename.', file=sys.stderr)
                        break
                    
                    chunk = data[len(FLCT_BYTES):]
                    received_bytes += len(chunk)
                    fd.write(chunk)

                    percentage = 100 * received_bytes / filesize
                    
                    if percentage >= percentage_step:
                        print('INFO received {}%'.format(percentage_step), end='\r')
                        percentage_step += 10
                    
                if data.startswith(FLCT_FINISHED):
                    fd.close()
                    print('INFO file {} saved.'.format(filename))
                    break
            
            print('INFO received 100%')
            
        except Exception as ex:
            print('ERROR {}: {}.'.format(ex.__class__.__name__, ex))

        print('INFO connection close.')
        conn.close()


if __name__=='__main__':
    server_mode(PORT)