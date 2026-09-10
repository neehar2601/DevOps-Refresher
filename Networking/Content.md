NICs
Network Interface Cards (NICs) connect devices to the network. Network adapter or network card are both alternate names for NICs. The NIC serves as an interface between a computer and the network. To connect to a network, a computer must have a NIC installed. 

NICs can be built into the motherboard of the computer or can be connected using a port on the device. NICs can connect to either wired or wireless networks.


Duplex
Historically, NICs had to have their duplex set. The term duplex refers to how the network cards handle two-way communication. There were two settings for duplex: half-duplex or full duplex.

In half-duplex communication, the NIC can both send and receive. But it can’t do both at the same time. NICs that are set to half-duplex function like a walkie talkie. 

In full duplex, NICs can both send and receive at the same time.

The most important thing about duplex is that both devices need to be using the same setting. Imagine one device is set to half-duplex and the other is set to full duplex. The full duplex NIC can send and receive at the same time. Therefore, it will never stop transmitting. The half-duplex NIC expects that it will either be sending or receiving. Since the full duplex NIC on the other side never stops transmitting, the half-duplex NIC never gets a chance to transmit at all.

Modern network cards, and the devices they connect to, support auto-sensing. If the device on the other side requires half-duplex, they will select half-duplex. If the device on the other side supports full duplex, they will select full duplex. You should not have to adjust duplex in your career, but it is something you can check if two devices are having trouble communicating.


MAC Addresses
To deliver something like mail or data, the recipient must have a unique address. Imagine if there were two houses that had the same address. How would the mail system know where to deliver each letter or package?

The same is true for NICs. Each NIC must have a unique address. That address is called a Media Access Control or MAC address. It may also be called a physical address. The MAC address is a unique, hardware address assigned to the NIC by the manufacturer. 

MAC addresses are 48 bits long. MAC addresses have six sets of two-digit hexadecimal numbers. The first three sets identify the manufacturer, and the last three sets identify that particular NIC. 


Hubs
It’s possible to connect two devices with a wire (or wireless) like you did in the Network Theory lab. However, networks usually have a lot more than two devices. In Ethernet networks, the network typically uses a central device to connect all the nodes. This redistribution point takes the data coming in and sends it to the receiving nodes. When all the nodes are connected to a central device, this is known as a star physical topology.


Early networks used devices called hubs. Hubs are also known as repeaters. That’s because these Layer 1 devices take the incoming signals and send it to all the ports on the hub. 

The only problem with hubs is caused by the very nature of how they work. If a node sends data to the hub, it repeats the data to all the ports. That means that if any other node was about to transmit, there will be a collision. Then both nodes will have to wait for a random time delay. The more devices connected to the hub, the more collisions the hub will have. The more collisions on the network, the slower the network runs. “Collision domain” is the term that describes all the nodes who can create a collision with each other. When you use a hub, all the devices are in one big collision domain.

Modern networks don’t use hubs, they use switches.


Switches
Switches can also receive incoming data and send it to other nodes. When the switch first turns on, it acts like a hub. It sends all the data to all the nodes. This is called “flooding” the data. 

To properly address data, the sending node must find the receiving node’s MAC address. Typically, the sending node has only the IP address of the receiving node. To find the MAC address of the NIC with a particular IP address, nodes use a protocol called Address Resolution Protocol (ARP). 

To resolve the receiving node’s IP address to its MAC address, the sending computer sends out an ARP broadcast. Suppose the sending computer needed to know the MAC address of a receiving computer with an IP address of 192.168.1.10. It would send an ARP broadcast, “192.168.1.10 what is your MAC address?” The switch sends all broadcasts to all ports. If 192.168.1.10 is on the network, the ARP broadcast reaches the device. It responds by providing the sending device with its MAC address.

As ARP broadcasts go through the switch, the switch makes a note of which MAC address(es) are on each port. The switch stores this information in its Content Addressable Memory (CAM) table. When data comes in, the switch looks at the destination MAC address. If the CAM table lists a port for that MAC address, the switch sends the data just to that one port. Because switches send data based on the MAC address, they are Layer 2 devices.

Because switches send the data to just the one port with the receiving node, that is the only device that could have a collision with the data. Therefore, each port on the switch is a separate collision domain.

Replacing a hub, where all the ports are one big collision domain, with a switch, where each port is a collision domain, can really speed up a network.


Managed Switches
Managed switches have firmware. The firmware functions as an operating system that can be used to program the switch with security features. 


Packet Sniffers
Packet Sniffers allow administrators to capture network traffic. Then the administrator can examine the actual data passing across the network. 

To capture traffic, the switch needs to send the data to the packet sniffer. However, the switch will only send data to the packet sniffer if the sniffer’s MAC address is listed as the receiving node.

To allow packet sniffers to collect all the data on a switch, administrators must configure port mirroring on the switch. This tells the switch to copy (mirror) all the data passing through the switch to one port. 

By default, NICs ignore data that is not either a broadcast or addressed to their MAC address. When administrators install a packet sniffer on a computer, they must tell the NIC to process all the incoming data even if it’s not a broadcast or addressed to the node’s NIC. They do this by putting the NIC into promiscuous mode. In promiscuous mode, the NIC sends all the data up the protocol stack to the packet sniffer.


Technically, any device that is connected to two or more different networks, and can pass information between them, is a router. Routers connect multiple networks that use the same protocol. Routers only work with routable protocols. Routable protocols assign an address to the network and to each node on the network. TCP/IP is a routable protocol. With IP addresses, part of the IP address is the network address. The remaining part is the node address.

All devices that support TCP/IP have a routing table. In a node that isn’t a router, the routing table lists the address of the local network. It also lists the default gateway, the address of the local router. The device uses the routing table to make routing decisions. Data that’s destined for the local network is sent directly to the destination device. 

When data comes in that’s destined for a different network, nodes send the data to the default gateway. The router uses the network address portion of the destination IP to decide what to do with the data. If that router isn’t directly connected to the destination network, it sends the data to another router. The data is delivered when it finally reaches a router connected to the destination network. 

Routers have more entries than nodes in their routing tables. By default, every device lists the local network in their routing tables. Routers exchange their routing tables with other routers. In that way, routers “learn” about other networks. Then they can forward data to remote networks.

When a broadcast comes into a network card on a router, the router knows that the broadcast was intended for all the nodes on that network. Broadcasts are not intended for nodes on other networks. That is why routers do not forward broadcasts. A broadcast domain is composed of all the nodes on one network. Routers separate broadcast domains.

A router can be a dedicated device, incorporated into a multi- function device, or can be implemented as software. Even a regular computer, with two NICs, can be configured as a router. Typically, when professionals use the term router, they’re talking about a dedicated device.