from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time
from mininet.node import Controller
import os
import sys
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch

hosts = []
switches = []
links = []
switch_name =[]
host_name = []

def top(x,y):
	net = Mininet(autoStaticArp=True, link=TCLink)
	hosts_per_switch = x/y
	""" Appending names of switches and hosts in list"""
	for i in range(0,y):
		switch_name.append('s'+str(i+1))
	for i in range(0,x):
		host_name.append('h'+str(i+1))

	info("**** Adding Controller ****\n")
	net.addController('c0')

	info("**** Adding Hosts ****\n")
	
	for i in range(x):
		if i%2==0:
			hosts.append(net.addHost(host_name[i], ip='10.0.0'+str(i+1) ))
			
		else:
			hosts.append(net.addHost(host_name[i], ip='11.0.0'+str(i+1) ))
			

	info("**** Adding Switches ****\n")
	for i in range(y):
		switches.append(net.addSwitch(switch_name[i],cls=OVSSwitch))


	info("**** Adding Links ****\n")
	k = 0
	for i in range(y):
		for j in range(hosts_per_switch):
			links.append(net.addLink(hosts[k], switches[i]))
			k += 1

	info('**** Allocating Bandwidth ****\n')
	
	for i in range(len(links)):
		if i%2==0:
			links[i].intf1.config(bw=1)
		else:
			links[i].intf1.config(bw=2)

	for i in range(y-1):
		links.append(net.addLink(switches[i], switches[i+1]))
	links.append(net.addLink(switches[y-1],switches[0]))

	info('**** Starting Network ****\n')
	net.start()
	"""
	 Enabling Spanning Tree Protocol On switches
	 It is of utmost importance if we are to avoid flooding of packets
	 Make sure to add this after you have started your network
	"""
	for i in range(y):
		switches[i].cmd('ifconfig '+switch_name[i]+' 10.0.1.'+str(i+1))

	for i in range(y):
		switches[i].cmd('ovs-vsctl set bridge '+switch_name[i]+' stp-enable=true')

	info('**** Running CLI ****\n')
	CLI(net)

	info('**** Stopping Network ****\n')
	net.stop()

if __name__ == '__main__':
	print "Enter Number of hosts"
	x = int(input())
	print "Enter Number of switches"
	y = int(input())
	setLogLevel('info')
	top(x,y)
