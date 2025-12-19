# CompTIA Network  N10-007 Cert Guide
- Author: Certification Guide
---
> ARP is a broadcast-based protocol and, therefore, does not travel beyond the local subnet of the sender
- Page 249
- Date Added: 2024-02-27 15:57:04
---
> As shown in the preceding example, routers rely on their internal routing table to make packet-forwarding decisions. Therefore, at this point, a logical question is, “How does a router’s routing table become populated with entries?” This is the focus of the next section
- Page 251
- Date Added: 2024-02-27 15:58:01
---
> As an administrator, you could statically configure a route entry
- Page 251
- Date Added: 2024-02-27 15:58:14
---
> As an administrator, you could statically configure a route entry. A route could be learned via a dynamic routing protocol (for example, OSPF or EIGRP)
- Page 251
- Date Added: 2024-02-27 15:58:31
---
> static routing does not scale well
- Page 253
- Date Added: 2024-02-27 16:00:06
---
> If a network is running more than one routing protocol (maybe as a result of a corporate merger), and a router receives two route advertisements from different routing protocols for the same network, which route advertisement does the router believe? Interestingly, some routing protocols are considered to be more believable that others. An example would be a Cisco router considering EIGRP to be more believable than RIP
- Page 255
- Date Added: 2024-02-27 16:01:00
---
> The AP connects to the wired LAN, and the wireless devices that connect to the wired LAN via the AP are on the same subnet as the AP. (No Network Address Translation [NAT] or PAT is being performed
- Page 317
- Date Added: 2024-03-05 07:51:25
---
> To manage multiple APs, a company will use a wireless LAN controller
- Page 317
- Date Added: 2024-03-05 07:51:38
---
> Antennas The coverage area of a WLAN is largely determined by the type of antenna used on a wireless AP or a wireless router
- Page 317
- Date Added: 2024-03-05 07:51:52
---
> Design goals to keep in mind when selecting an antenna include the following
- Page 318
- Date Added: 2024-03-05 07:52:05
---
> The strength of the electromagnetic waves being radiated from an antenna is referred to as gain
- Page 318
- Date Added: 2024-03-05 07:52:13
---
> Gain is commonly measured using the dBi unit of measure. In this unit of measure, the dB stands for decibels and the i stands for isotropic. A decibel, in this context, is a ratio of radiated power to a reference value. In the case of dBi, the reference value is the signal strength (power) radiated from an isotropic antenna
- Page 318
- Date Added: 2024-03-05 07:52:56
---
> Later in this chapter, you are introduced to a variety of wireless standards, which are all variants of the IEEE 802.11 standard. As you contrast one standard with another, a characteristic to watch out for is the frequencies at which these standards operate. Although there are some country-specific variations, certain frequency ranges (or frequency bands) have been reserved internationally for industrial, scientific, and medical purposes. These frequency bands are called the ISM bands, where ISM derives from industrial, scientific, and medical
- Page 320
- Date Added: 2024-03-05 07:54:25
---
> WLANs use the range of frequencies in the 2.4GHz-to-2.5GHz
- Page 320
- Date Added: 2024-03-05 07:54:34
---
> CSMA/CA is needed for WLAN connections because of their half-duplex operation
- Page 323
- Date Added: 2024-03-05 07:56:02
---
> the collision-avoidance part of the CSMA/CA algorithm causes wireless devices to wait for a random back-off time before transmitting
- Page 323
- Date Added: 2024-03-05 07:56:28
---
> center frequencies of a channel. In actual operation, a channel uses more than one frequency, which is a transmission method called spread spectrum
- Page 323
- Date Added: 2024-03-05 07:56:53
---
> if a third party intercepted a DSSS transmission, it would be difficult for them to eavesdrop on the data because they would not easily know which chips represented valid bits
- Page 324
- Date Added: 2024-03-05 07:57:56
---
> WLAN Standards Most modern WLAN standards are variations of the original IEEE 802.11 standard
- Page 324
- Date Added: 2024-03-05 07:58:33
---
> MIMO uses multiple antennas for transmission and reception. These antennas do not interfere with one another, thanks to MIMO’s use of spatial multiplexing
- Page 325
- Date Added: 2024-03-05 08:02:46
---
> Yet another technology implemented by 802.11n is channel bonding. With channel bonding, two wireless bands are logically bonded together, forming a band with twice the bandwidth of an individual band. Some literature refers to channel bonding as 40MHz mode, which is the bonding of two adjacent 20MHz bands into a 40MHz band
- Page 325
- Date Added: 2024-03-05 08:03:04
---
> Types of WLANs WLANs can be categorized based on their use of wireless APs
- Page 326
- Date Added: 2024-03-05 08:03:34
---
> A major issue for WLANs is radio frequency interference (RFI) caused by other devices using similar frequencies to the WLAN devices
- Page 329
- Date Added: 2024-03-05 08:04:26
---
> if you need cordless phones to coexist in an environment with WLAN devices using the 2.4GHz band, consider the use of digital enhanced cordless telecommunications (DECT
- Page 330
- Date Added: 2024-03-05 08:04:59
---
> most RFI occurs in the 2.4GHz band as opposed to the 5GHz band
- Page 330
- Date Added: 2024-03-05 08:07:16
---
> uptime, is a major design consideration
- Page 345
- Date Added: 2024-03-05 08:10:28
---
> . Be careful not to confuse availability with reliability. A reliable network, as an example, does not drop many packets, whereas an available network is up and operational
- Page 345
- Date Added: 2024-03-05 08:11:21
---
> When designing networks for high availability, answer the following questions
- Page 349
- Date Added: 2024-03-05 08:13:59
---
> Consider water flowing through a series of pipes with varying diameters. The water’s flow rate through those pipes is limited to the water’s flow rate through the pipe with the smallest diameter. Similarly, as a packet travels from its source to its destination, its effective bandwidth is the bandwidth of the slowest link along that path. For example, consider Figure 9-7. Notice that the slowest
- Page 352
- Date Added: 2024-03-05 08:17:29
---
> QoS Configuration Steps The mission statement of QoS could read something like this: “To categorize traffic and apply a policy to those traffic categories, in accordance with a QoS policy.” Understanding this underlying purpose of QoS can help you better understand the three basic steps to QoS configuration
- Page 353
- Date Added: 2024-03-05 08:27:41
---
> As previously mentioned, a DiffServ approach to QoS marks traffic. However, for markings to impact the behavior of traffic, a QoS tool must reference those markings and alter the packets’ treatment
- Page 355
- Date Added: 2024-03-05 08:28:43
---
> Classification is the process of placing traffic into different categories. Multiple characteristics
- Page 356
- Date Added: 2024-03-05 08:28:53
---
> Marking alters bits within a frame, cell, or packet to indicate how the network should treat that traffic. Marking alone does not change how the network treats a packet. Other tools (such as queuing tools) can, however, reference those markings and make decisions based on the markings
- Page 356
- Date Added: 2024-03-05 08:29:11
---
> improper wiring might function immediately following an installation; however, over time, the wiring might start to experience intermittent issues that cause network disruptions
- Page 415
- Date Added: 2024-03-07 09:08:02
---
> Interference on a transmission medium, or faulty cabling, can cause errors in the transmission of binary data (or bits). A common measurement for bit errors is called bit error rate (BER), which is calculated as follows: BER = Bit errors / Bits transmitted For example, imagine that a network
- Page 416
- Date Added: 2024-03-07 09:08:22
---
> To prevent such an occurrence, you can use environmental monitors to send an alert if the temperature in a room rises above or drops below administratively configured
- Page 420
- Date Added: 2024-03-07 09:12:58
---
