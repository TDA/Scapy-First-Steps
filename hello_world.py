__author__ = 'saipc'

from scapy.all import *

a = IP(src = '127.0.0.1', ttl = 64647)
print a.ttl
print a.src

print a.dst

a.dst = '192.168.1.1'
print a.dst
#
# # print a
#
del(a.ttl)
#
# # print a
#
print a.ttl
#
target = "www.target.com/30"
ip = IP(dst = target)
print ip.dst
ips = [i for i in ip]
print ips
#
c=TCP(dport=443)
ip_c = [p for p in ip/c]
print ip_c
send(IP(src="127.0.0.1",dst="127.0.0.1", ttl = 128)/ICMP()/"Hello World")
send(IP(src="127.0.0.1",dst="127.0.0.1", ttl = 128)/TCP(sport = 2220, dport=80)/"Hello World")
send(IP(src="127.0.0.1",dst="127.0.0.1", ttl = 128)/UDP()/"Hello World")
# send(IP(dst="127.0.0.1", src="127.0.0.1", ttl = 212)/UDP(sport=55555, dport=53)/"boo its me! an ethernet ghost!")