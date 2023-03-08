from scapy.all import *
import time, sys
from datetime import datetime, date

pkts = rdpcap(sys.argv[1])
clk = pkts[0].time
for p in pkts:
    val = p.time - clk
    time.sleep(int(val))
    clk = p.time
    sendp(p, iface=sys.argv[2])
