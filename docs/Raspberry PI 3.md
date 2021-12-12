### Raspberry PI 3
(cat /proc/cpuinfo)
 
         Processors : 4
         model name : ARMv7 Processor rev 4 (v7l)
           BogoMIPS : 57.60
           Features : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
    CPU implementer : 0x41
   CPU architecture : 7
        CPU variant : 0x0
           CPU part : 0xd03
       CPU revision : 4

 
Hardware            : BCM2835

Revision              : a02082

Serial                    : 00000000b0efcb08

Model                  : Raspberry Pi 3 Model B Rev 1.2

 
(cat /proc/meminfo)

MemTotal: 876176 kB

 
OS:

(cat /etc/os-release)

 
NAME="Ubuntu"

VERSION="18.04.6 LTS (Bionic Beaver)"

ID=ubuntu

ID_LIKE=debian

PRETTY_NAME="Ubuntu 18.04.6 LTS"

VERSION_ID="18.04"

VERSION_CODENAME=bionic

UBUNTU_CODENAME=bionic
 
(lsb_release -a)

No LSB modules are available.

Distributor ID:   Ubuntu

Description:        Ubuntu 18.04.6 LTS

Release:              18.04

Codename:         bionic

 
(hostnamectl)

    Static hostname: utad 
          Icon name: computer        
         Machine ID: 17642ad8b86c40e7a23ee63a6d24d4ad        
            Boot ID: 252b8a7a773a4e8bb00e9d6c9e3b4cef           
   Operating System: Ubuntu 18.04.6 LTS  
             Kernel: Linux 5.4.0-1042-raspi          
       Architecture: arm


