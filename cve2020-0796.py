# Original code: https://github.com/ollypwn/SMBGhost/blob/master
#
# Updated by Knightmare/ 8balla / MinatoTW to support CID masks

import socket
import struct
import sys
from netaddr import IPNetwork

subnet = sys.argv[1]

for ip in IPNetwork(subnet):

  pkt = b'\x00\x00\x00\xc0\xfeSMB@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x08\x00\x01\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\x02\x02\x10\x02"\x02$\x02\x00\x03\x02\x03\x10\x03\x11\x03\x00\x00\x00\x00\x01\x00&\x00\x00\x00\x00\x00\x01\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\n\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(3)
  try :
    sock.connect(( str(ip),  445 ))
    sock.send(pkt)
  except:
    pass
#    print("Failed to connect")
    sock.close()
    continue
  nb, = struct.unpack(">I", sock.recv(4))
  res = sock.recv(nb)
  sock.close()
  if not res[68:70] == b"\x11\x03":
    pass
    print('%s Not vulnerable' % ip)
  elif not res[70:72] == b"\x02\x00":
    pass
    print('%s Not vulnerable' % ip)
  else: 
    pass
    print('%s Vulnerable!' % ip)
  sock.close()
