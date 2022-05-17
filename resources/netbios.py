import socket

def netbios_name(addr):
    '''
    easy hostname extraction
    '''
    data = b'ff\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00 CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00!\x00\x01'  # documentation
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.sendto(data, (addr, 137))
        rep = s.recv(2000)
        
        num = ord(rep[56:57].decode())          # extract number of pieces received
        data = rep[57:]
        
        for i in range(num):
            name = data[18 * i:18 *i + 15].decode()                 # extract name than check for a valid one
            flag_bit = bytes(data[18 * i + 15:18 *i + 16])
            name_flags = data[18 * i + 16:18 *i + 18]
            if flag_bit in b'\x00':                                 # define wich is valid
                if ord(name_flags[0:1])<128:
                    return name.strip()
    except: 
        return ''   # hostname not detected
