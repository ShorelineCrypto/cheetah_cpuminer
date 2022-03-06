# cheeta_cpuminer

## Cheetah_Cpuminer for Cheetahcoin (CHTA) 

* How to Install Cheetah_Cpuminer for Cheetahcoin (CHTA)? 

Warning: this software only works on older verison of python 2.7 or python2. This software will not work in newest python 3 versions.

github branch of "chta" of below repos:
https://github.com/ShorelineCrypto/cheetah_cpuminer/tree/chta

Under command line with git. run below to access this branch for CHTA for linux/mac bash shell:

```
  git clone https://github.com/ShorelineCrypto/cheetah_cpuminer cheetah_cpuminer_chta
  cd cheetah_cpuminer_chta
  git pull
  git checkout chta
```

Or download directly on zip file of "chta-beta2" release:
https://github.com/ShorelineCrypto/cheetah_cpuminer/releases/tag/chta-beta2


## What is Cheetah_Cpuminer?

Cheetahcoin (CHTA) blockchain has 3rd generation dynamic difficulty adjustment algorithm "randomSpike"
which may trigger ASIC miners to get stuck on CHTA blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC/GPU miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.1.5 is tested under Windows 10, macOS El Capitan (10.11), macOS Mojave (10.14), macOS Catelina (10.15) and 8 distros of Linux (Ubuntu 16.04/18.04/20.04, Debian 9/10, MX Linux, Linux Mint, Fedora, openSUSE, Arch/Manjaro).
 - Other versions of Windows, Mac or Linux platform are untested.  Cheetah under other windows, mac, linux may still work. For example windows full node CHTA wallet was tested to be working windows XP.  Python based cheetah typically works on any version of unix, windows, or macOS. The limitation tends to be the full node wallet software for Cheetahcoin, which is required for the in-wallet mining operation.  If you can run a full node on whatever flavor of unix or mac, or windows, cheetah_cpuminer will work. 


## CPU Minable Coin - Cheetahcoin (CHTA)
Because of randomSpike algorithm on top of SHA256, Cheetahcoin is CPU Minable. Users can easily set up  full node for mining at Home Windows PC, Mac, Linux, Chromebook or android phones using this open sourced cheetah software.  

Research on the first forked 50 blocks on v1.2.0 core confirmed that ASIC/GPU miners mined 66% of 50 blocks, CPU miners mined the remaining 34%.

## Android Mining with Cheetah_Cpuminer

Android phone (64 bits arm64 or32 bits armhf) has a slightly different operation workflow compared to computers. Please check out web guide for Android CPU Mining through UserLand app at:
https://github.com/ShorelineCrypto/CheetahCoin/tree/master/doc/Android_Userland_App

The Cheetah CPU mining operation portion of Android mining setup is actually same as below desktop/laptop linux guides. Instead of running cheetah in computer terminal, 
you run cheetah inside android UserLand app's linux terminal. 

## Chromebook Mining with Cheetah_Cpuminer

Chromebook (x64 or arm) has a slightly different operation workflow compared to computers. Please check out web guide for Chromebook CPU Mining through Linux (beta) app at:
https://github.com/ShorelineCrypto/CheetahCoin/tree/master/doc/Chromebook

The Cheetah CPU mining operation portion of Chromebook mining setup is actually same as below desktop/laptop linux guides. Instead of running cheetah in computer terminal, 
you run cheetah inside chromebook's linux terminal. 


## Linux - Ubuntu/Debian/MX Linux/Linux Mint/Arch/Manjaro/Fedora/openSUSE

### How to Install Cheetah_Cpuminer

 - Under supported version linux, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
``` 
     curl https://bootstrap.pypa.io/pip/2.7/get-pip.py  -o get-pip.py
     sudo  python2 get-pip.py
```
In new linux distro versions,  the python 2.7 is python2 , pip2 is used to avoid confusion with python3

```
     sudo pip2 install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run Cheetahcoin linux wallet first (command line or QT either one) from release page at:
 https://github.com/ShorelineCrypto/CheetahCoin/releases
 - At the same local linux machine, using the provided cheetahcoin example, modify rpc username password change the filename 
 into 'cheetahcoin.conf' , run below command:
```
            cp cheetahcoin.conf  ~/.cheetahcoin/
```
 -  Restart wallet.   Fully sync the wallet to latest block. A full node of CHTA is required to allow Cheetah_Cpuminer to work.
 - run below command using the provided the bash shell script:
```
            sh cheetah.sh
```
 or more customized command line like below:
```
    python2 main.py  --interval  10  --cpu 4
```
 - Optimization of CPU mining on cheetah.sh file: see below windows section for detailed recommendation. 
 
 
 ## MacOS 10.11 El Capitan or higher 

### How to Install Cheetah_Cpuminer

 - Under macOS terminal, install pip if it is not there:

```
 curl https://bootstrap.pypa.io/pip/2.7/get-pip.py  -o get-pip.py
 sudo  python2 get-pip.py
```

 - Under macOS terminal, run below command to install python-bitcoinrpc  ( https://github.com/jgarzik/python-bitcoinrpc ):
 
``` 
     sudo pip2 install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run Cheetahcoin mac wallet first (CLI or GUI either one).  Please be aware that additional library files are required to be installed or dmg installed GUI/CLI wallet won't work
 without them.  macOS Mojave wallet has detailed library dependencies installation guide at:
 https://github.com/ShorelineCrypto/CheetahCoin/releases/download/v1.2.1.2/cheetahcoin_v1.2.1.2_macOS_Mojave.tgz
 After proper dependencies are installed for macOS, the El Capitan wallet files (CLI or dmg file) should work for all the macOS platforms from version 10.11 or later. 
 
 macO versions of macOS from 10.11 to 10.14 or earlier or later 
 - At the same local mac machine, using the provided "cheetahcoin.conf-example" example file, modify rpcusername rpcpassword fields value with an editor,  change the filename into 'cheetahcoin.conf' , run below command in mac terminal:
```
            cp  cheetahcoin.conf  ~/Library/'Application Support'/Cheetahcoin/
```
 -  Restart wallet.   Fully sync the wallet to latest block. A full node of CHTA is required to allow Cheetah_Cpuminer to work.
 - run below command using the provided the bash shell script:
```
            sh cheetah.sh
```
 - Optimization of CPU mining on cheetah.sh file: see below windows section for detailed recommendation. 
 
 
 ## Windows 10, XP or higher

### How to Install Cheetah_Cpuminer

 - Download v2.7.x version of windows python from https://www.python.org/downloads/windows/ and install it.
 - Open a window command prompt terminal, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
```
     set PATH=C:\Python27;C:\Python27\Scripts;%PATH%
     pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run Cheetahcoin Windows QT wallet. 
 - At the same local machine, using the provided "cheetahcoin.conf-example" example file, modify rpcusername rpcpassword fields value with wordpad,  change the filename 
 into 'cheetahcoin.conf' ,  copy 'cheetahcoin.conf'  to your path 'C:\Users\YourUser\AppData\Roaming\Cheetahcoin'
 - Restart wallet.   Fully sync the wallet to latest block. A running full node of CHTA is required to allow Cheetah_Cpuminer to work.
 - Download and unpack the latest Cheetah_Cpuminer release from https://github.com/ShorelineCrypto/cheetah_cpuminer/releases
 - Double click the provided window batch file 'cheetah.bat' to start CPU mining.
 
 #### Note for Windows CPU Miners
 - Even if the wallet is fully synced under window machine, you may have to  double click the bat file,  stay for couple of minutes and then close it, and restart it again to allow cheetah to work properly.  Somehow cheetah bat file may not work with the first try. 
 
 
 ## Optimization for CPU solo mining with Cheetah
 - change window bat file or linux/mac sh file based on your machine CPU core number.  Recommends 2 cpu for 4 core Intel PC/Mac, 6 cpu for 8 core PC/Mac.
 For interval you may shortern it to a number such as 10, meaning the software cheetah will check full node blockchain every 10 seconds to determine to start or stop mining.
 - Example of a full command assuming 10 secondes interval and 2 core cpu in "cheetah.bat" file or "cheetah.sh" file

```
     python main.py --interval 10 --cpu 2
```

In newer version of Linux or MacOS, many times the python 2.7 path is "python2" so that the command should be:

```
     python2 main.py --interval 10 --cpu 2
```


## License


Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


