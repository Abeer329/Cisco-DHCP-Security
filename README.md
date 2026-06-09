# Cisco-DHCP-Security
DHCP Security Lab: DHCP Starvation, Rogue DHCP, DHCP Snooping, and Rate Limiting in a Cisco GNS3 environment
DHCP Security Lab

Overview

This project demonstrates common DHCP-related attacks and security controls in a Cisco lab environment.

Attacks Demonstrated

DHCP Starvation Attack
Rogue DHCP Server Attack
Security Controls

DHCP Snooping
Trusted Ports
DHCP Rate Limiting
Lab Environment

Tools Used

GNS3
Cisco vIOS Router
Cisco vIOS Switch
Kali Linux
Wireshark
Python (Scapy)
Network Topology

Attacker and Client are connected to the same Layer 2 switch.

The switch is connected to the legitimate DHCP server (Cisco Router).

Attack Scenario 1: DHCP Starvation

A custom Scapy script was used to generate DHCP Discover messages with randomized MAC addresses.

Result:

DHCP leases were consumed rapidly.
DHCP server resources were affected.
Attack Scenario 2: Rogue DHCP

A rogue DHCP server was deployed in the lab environment.

Result:

Clients received unauthorized DHCP configuration.
Incorrect gateway and network settings were assigned.
Mitigation

DHCP Snooping

DHCP Snooping was enabled on the switch to block unauthorized DHCP servers.

Rate Limiting

Rate limiting was configured on untrusted ports to reduce the impact of DHCP starvation attacks.

Results

After implementing security controls:

Rogue DHCP responses were blocked.
DHCP starvation impact was reduced.
DHCP infrastructure was protected.
Network availability was improved.
Repository Structure

screenshots/

topology.png
dhcp-starvation-attack.png
rogue-dhcp-attack.png
dhcp-snooping-config.png
attack-mitigated.png
configs/

router-dhcp-config.txt
switch-security-config.txt
scripts/

dhcp_starvation.py.
