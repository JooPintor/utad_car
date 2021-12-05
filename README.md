# tese
Esta pagina tem o objectivo de ser um depositorio de conhecimento para o ensino de utilização de ROS e introdução de visão a robos, os sucessus e fracasso enquanto á sua utilização e emplemtação com o material utilizado listado nas alinhas a seguir.

- O que é ROS?\n
Robot Operating System é o sistema mais utilizados nos ultimos anos quando se vem há robotica, sendo este uma framework crianda a partir da ligação de diferentes computadores que assim vai criar o seu proprio sistema operativo para o robo que está a ser programado, para comprir as suas funções.

- Material utilizado
Rasperry Pi 3: Ubuntu Rob3: Linux verº18.04: ROS-melodic:
SBC (Single Board Computers)
 
Raspberry PI 3
cat /proc/cpuinfo
 
Processors: 4
model name      : ARMv7 Processor rev 4 (v7l)
BogoMIPS           : 57.60
Features              : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32
CPU implementer            : 0x41
CPU architecture: 7
CPU variant        : 0x0
CPU part             : 0xd03
CPU revision       : 4
 
Hardware            : BCM2835
Revision              : a02082
Serial                    : 00000000b0efcb08
Model                  : Raspberry Pi 3 Model B Rev 1.2
 
cat /proc/meminfo
MemTotal: 876176 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 18.04.6 LTS
Release:              18.04
Codename:         bionic
 
hostnamectl
   Static hostname: utad
         Icon name: computer
        Machine ID: 17642ad8b86c40e7a23ee63a6d24d4ad
           Boot ID: 252b8a7a773a4e8bb00e9d6c9e3b4cef
  Operating System: Ubuntu 18.04.6 LTS
            Kernel: Linux 5.4.0-1042-raspi
      Architecture: arm



Rapsperry Pi 4: Linux verº20.07: ROS-noetic
Raspberry PI 4
cat /proc/cpuinfo
 
Model                  : Raspberry Pi 4 Model B Rev 1.
Processors: 4
BogoMIPS           : 108.00
Features              : fp asimd evtstrm crc32 cpuid
CPU implementer            : 0x41
CPU architecture: 8
CPU variant        : 0x0
CPU part             : 0xd08
CPU revision       : 3
 
Hardware            : BCM2835
Revision              : c03112
Serial                    : 1000000077cc0d0c
Model                  : Raspberry Pi 4 Model B Rev 1.2
 
cat /proc/meminfo
MemTotal:        3884324 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="20.04.2 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.2 LTS"
VERSION_ID="20.04"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 20.04.2 LTS
Release:              20.04
Codename:         focal
 
hostnamectl
   Static hostname: rpi4
         Icon name: computer
        Machine ID: 0f314813462c45599e46b4825c222602
           Boot ID: 45fe831cc2764fa48426dac216f3a48e
  Operating System: Ubuntu 20.04.2 LTS
            Kernel: Linux 5.4.0-1044-raspi
      Architecture: arm64

Nvidia Jetson Nano 2GB develepor kit: Ubuntu Rob3: Linux verº18.04: ROS-melodic
model name      : ARMv8 Processor rev 1 (v8l)
Processors: 4
 
BogoMIPS           : 38.40
Features              : fp asimd evtstrm aes pmull sha1 sha2 crc32
CPU implementer            : 0x41
CPU architecture: 8
CPU variant        : 0x1
CPU part             : 0xd07
CPU revision       : 1
 
cat /proc/meminfo
MemTotal:        2027380 kB
 
OS:
cat /etc/os-release
 
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic                                                                              
 
lsb_release -a
No LSB modules are available.
Distributor ID:   Ubuntu
Description:        Ubuntu 18.04.5 LTS
Release:              18.04
Codename:         bionic
 
hostnamectl
   Static hostname: nvidia
         Icon name: computer
        Machine ID: a3d9197b765643568af09eb2bd3e5ce7
           Boot ID: bca3a94ac6a84bf7a3760e89f6eb2f61
  Operating System: Ubuntu 18.04.5 LTS
            Kernel: Linux 4.9.201-tegra
      Architecture: arm64


Portátil ASUSLaptop X512DA.313, 24/8/2020: Microsoft Windows 10 Home verº10.0.19043: ROS-melodic

OS Name:                   Microsoft Windows 10 Home
OS Version:                10.0.19043 N/A Build 19043
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Product ID:                00325-81937-05138-AAOEM
Original Install Date:     03/11/2020, 01:58:26
System Boot Time:          26/09/2021, 15:40:39
System Manufacturer:       ASUSTeK COMPUTER INC.
System Model:              VivoBook_ASUSLaptop X512DA_F512DA
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: AMD64 Family 23 Model 24 Stepping 1 AuthenticAMD ~2100 Mhz
BIOS Version:              American Megatrends Inc. X512DA.313, 24/08/2020
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             pt;Português (Portugal)
Input Locale:              pt;Português (Portugal)
Time Zone:                 (UTC+00:00) Dublin, Edimburgo, Lisboa, Londres
Total Physical Memory:     5 068 MB
Available Physical Memory: 1 438 MB
Virtual Memory: Max Size:  7 116 MB
Virtual Memory: Available: 1 642 MB
Virtual Memory: In Use:    5 474 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\HB
Hotfix(s):                 13 Hotfix(s) Installed.
                           [01]: KB5004331
                           [02]: KB4534170
                           [03]: KB4537759
                           [04]: KB4542335
                           [05]: KB4545706
                           [06]: KB4577586
                           [07]: KB4580325
                           [08]: KB4586864
                           [09]: KB4589212
                           [10]: KB4598481
                           [11]: KB5000736
                           [12]: KB5005565
                           [13]: KB5005699
Network Card(s):           2 NIC(s) Installed.
                           [01]: Qualcomm Atheros QCA9377 Wireless Network Adapter
                                 Connection Name: Wi-Fi
                                 DHCP Enabled:    Yes
                                 DHCP Server:     192.168.1.1
                                 IP address(es)
                                 [01]: 192.168.1.35
                                 [02]: fe80::95fb:61cd:d25e:e483
                           [02]: Bluetooth Device (Personal Area Network)
                                 Connection Name: Ligação de Rede Bluetooth
                                 Status:          Media disconnected
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.



- incluindo os links para fazer download
- Explicação de alguns dos processos
- Algumas das dificuldades encontradas
- A explicação de como funciona
- Resultados Esperados
