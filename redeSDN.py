# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
 net = Mininet(controller=Controller, switch=OVSSwitch)
    
# Adicionar o controlador
c0 = net.addController('c0')

# Adicionar as switches
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')

# Adicionar os hosts
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
h6 = net.addHost('h6')
h7 = net.addHost('h7')
h8 = net.addHost('h8')
h9 = net.addHost('h9')
h10 = net.addHost('h10')

# Conectar hosts às switches
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(h3, s2)
net.addLink(h4, s2)
net.addLink(h5, s3)
net.addLink(h6, s3)
net.addLink(h7, s4)
net.addLink(h8, s4)
net.addLink(h9, s5)
net.addLink(h10, s5)

# Conectar switches
net.addLink(s1, s2)
net.addLink(s2, s3)
net.addLink(s3, s4)
net.addLink(s4, s5)
net.addLink(s5, s1)
net.addLink(s2, s5)
net.addLink(s4, s1)

# Iniciar a rede
net.build()
c0.start()
s1.start([c0])
s2.start([c0])
s3.start([c0])
s4.start([c0])
s5.start([c0])

# Configurar os endereços IP para os hosts
h1.cmd('ifconfig h1-eth0 10.0.0.1 netmask 255.255.255.0')
h2.cmd('ifconfig h2-eth0 10.0.0.2 netmask 255.255.255.0')
h3.cmd('ifconfig h3-eth0 10.0.0.3 netmask 255.255.255.0')
h4.cmd('ifconfig h4-eth0 10.0.0.4 netmask 255.255.255.0')
h5.cmd('ifconfig h5-eth0 10.0.0.5 netmask 255.255.255.0')
h6.cmd('ifconfig h6-eth0 10.0.0.6 netmask 255.255.255.0')
h7.cmd('ifconfig h7-eth0 10.0.0.7 netmask 255.255.255.0')
h8.cmd('ifconfig h8-eth0 10.0.0.8 netmask 255.255.255.0')
h9.cmd('ifconfig h9-eth0 10.0.0.9 netmask 255.255.255.0')
h10.cmd('ifconfig h10-eth0 10.0.0.10 netmask 255.255.255.0')

# Definir o controlador para as switches
s1.cmd('ovs-vsctl set-controller s1 tcp:127.0.0.1:6633')
s2.cmd('ovs-vsctl set-controller s2 tcp:127.0.0.1:6633')
s3.cmd('ovs-vsctl set-controller s3 tcp:127.0.0.1:6633')
s4.cmd('ovs-vsctl set-controller s4 tcp:127.0.0.1:6633')
s5.cmd('ovs-vsctl set-controller s5 tcp:127.0.0.1:6633')
s6.cmd('ovs-vsctl set-controller s6 tcp:127.0.0.1:6633')
s7.cmd('ovs-vsctl set-controller s7 tcp:127.0.0.1:6633')
s8.cmd('ovs-vsctl set-controller s8 tcp:127.0.0.1:6633')
s9.cmd('ovs-vsctl set-controller s9 tcp:127.0.0.1:6633')
s10.cmd('ovs-vsctl set-controller s10 tcp:127.0.0.1:6633')

# Iniciar a interface de linha de comando
CLI(net)

# Parar a rede
net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    reate_network()