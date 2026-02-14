#!/usr/bin/env python3
import asyncio
import socket
import struct
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
TIMEOUT = 30

async def check():
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(True)
        sock.connect((HOST, PORT))
        
        # Send Hello packet
        hello = sys.argv[3]
        body = struct.pack('B', 1) + struct.pack('<B', len(hello)) + hello
        packet = struct.pack('<H', len(body) + 2) + body
        sock.sendall(packet)
        
        # Wait for RequestPassword (37) or PlayerInfo (3)
        buffer = b''
        sock.settimeout(TIMEOUT)
        
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buffer += data
            
            while len(buffer) >= 3:
                length = struct.unpack('<H', buffer[:2])[0]
                if len(buffer) < length:
                    break
                
                msg_type = buffer[2]
                buffer = buffer[length:]
                
                if msg_type in (3, 37):  # PlayerInfo or RequestPassword
                    with open('terraria_server_status', 'w+') as f:
                        f.write('online')
                    return 0
        
        with open('terraria_server_status', 'w+') as f:
            f.write('offline')
        return 1
        
    except Exception as e:
        with open('terraria_server_status', 'w+') as f:
            f.write('offline')
        raise e
        return 1
    finally:
        if sock:
            sock.close()

if __name__ == '__main__':
    sys.exit(asyncio.run(check()))
