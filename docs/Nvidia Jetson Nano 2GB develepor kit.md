### Nvidia Jetson Nano 2GB develepor kit

(cat /proc/cpuinfo)

          model name: ARMv8 Processor rev 1 (v8l)
          Processors: 4
            BogoMIPS: 38.40
            Features: fp asimd evtstrm aes pmull sha1 sha2 crc32
     CPU implementer: 0x41
    CPU architecture: 8
         CPU variant: 0x1
            CPU part: 0xd07
        CPU revision: 1
 

(cat /proc/meminfo)


           MemTotal: 2027380 kB

 
OS:
(cat /etc/os-release)

    
                NAME= "Ubuntu"
             VERSION= "18.04.5 LTS (Bionic Beaver)"
                  ID= ubuntu
             ID_LIKE= debian
         PRETTY_NAME= "Ubuntu 18.04.5 LTS"
          VERSION_ID= "18.04"
    VERSION_CODENAME= bionic
     UBUNTU_CODENAME= bionic
 
(lsb_release -a)

    No LSB modules are available.

      Distributor ID: Ubuntu
         Description: Ubuntu 18.04.5 LTS
             Release: 18.04
            Codename: bionic
 
(hostnamectl)

     Static hostname: nvidia
           Icon name: computer
          Machine ID: a3d9197b765643568af09eb2bd3e5ce7
             Boot ID: bca3a94ac6a84bf7a3760e89f6eb2f61
    Operating System: Ubuntu 18.04.5 LTS
              Kernel: Linux 4.9.201-tegra
        Architecture: arm64
