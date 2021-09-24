import time
from pysnmp import hlapi
from Snmp import get

def StreamReceivedPacketAmount():
    running = True
    while running:
        try:
            #Ask for packets in:
            output = get('10.10.1.2', ['.1.3.6.1.2.1.4.9.0'], hlapi.CommunityData('Class'))
            
            print(list(output.values())[0])
            time.sleep(3)
        except KeyboardInterrupt:
            running = False