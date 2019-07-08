# cheeta_cpuminer


## What is Cheetah_Cpuminer?

NewEnglandcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC/GPU miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.1.3 is tested under Windows 10, OS X 10.11 El Capitan, macOS Mojave 10.14.4 and Ubuntu 16.04/18.04.
 - Other versions of Windows, Mac or Linux platform are untested.  Cheetah under other windows (win64 ir win32), mac (OSX 10.7 or later) or linux (Debian, etc) may still work.
 Python based cheetah typically works on any version of unix. The limitation tends to be the full node wallet software for NewEnglandcoin, which is required for the in-wallet
 mining operation.  If you can run a full node on whatever flavor of unix or mac, or windows, cheetah_cpuminer will work. 


## Linux - Ubuntu 16.04/18.04

### How to Install Cheetah_Cpuminer

 - Under Ubuntu 16.04/18.04 based linux, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
``` 
     sudo pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run NewEnglandcoin linux wallet first (command line or QT either one) from release page at:
 https://github.com/ShorelineCrypto/NewEnglandCoin/releases
 - At the same local linux machine, using the provided newenglandcoin example, modify rpc username password change the filename 
 into 'newenglandcoin.conf' , run below command:
```
            cp newenglandcoin.conf  ~/.newenglandcoin/
```
 -  Restart wallet.   Fully sync the wallet to latest block. A full node of NENG is required to allow Cheetah_Cpuminer to work.
 - run below command using the provided the bash shell script:
```
            sh cheetah.sh
```
 or more customized command line like below:
```
    python main.py  --interval  10  --cpu 4
```
 - Optimization of CPU mining on cheetah.sh file: see below windows section for detailed recommendation. 
 
 
 ## MacOS El Capitan, Mojave, or any other versions in between

### How to Install Cheetah_Cpuminer

 - Under macOS terminal, install pip if it is not there:

```
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 sudo  python get-pip.py
```

 - Under macOS terminal, run below command to install python-bitcoinrpc  ( https://github.com/jgarzik/python-bitcoinrpc ):
 
``` 
     sudo pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run NewEnglandcoin mac wallet first (CLI or GUI either one).  Please be aware that additional library files are required to be installed or dmg installed GUI/CLI wallet won't work
 without them.  macOS Mojave wallet has detailed library dependencies installation guide at:
 https://github.com/ShorelineCrypto/NewEnglandCoin/releases/download/v1.2.1.2/newenglandcoin_v1.2.1.2_macOS_Mojave.tgz
 After proper dependencies are installed for macOS, the El Capitan wallet files (CLI or dmg file) should work for all the macOS platforms from version 10.11 or later. 
 
 macO versions of macOS from 10.11 to 10.14 or earlier or later 
 - At the same local mac machine, using the provided "newenglandcoin.conf-example" example file, modify rpcusername rpcpassword fields value with an editor,  change the filename into 'newenglandcoin.conf' , run below command in mac terminal:
```
            cp  newenglandcoin.conf  ~/Library/'Application Support'/NewEnglandcoin/
```
 -  Restart wallet.   Fully sync the wallet to latest block. A full node of NENG is required to allow Cheetah_Cpuminer to work.
 - run below command using the provided the bash shell script:
```
            sh cheetah.sh
```
 - Optimization of CPU mining on cheetah.sh file: see below windows section for detailed recommendation. 
 
 
 ## Windows 10

### How to Install Cheetah_Cpuminer

 - Download v2.7.x version of windows python from https://www.python.org/downloads/windows/ and install it.
 - Open a window command prompt terminal, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
```
     set PATH=%PATH%;C:\Python27;C:\Python27\Scripts
     pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run NewEnglandcoin Windows QT wallet. 
 - At the same local machine, using the provided "newenglandcoin.conf-example" example file, modify rpcusername rpcpassword fields value with wordpad,  change the filename 
 into 'newenglandcoin.conf' ,  copy 'newenglandcoin.conf'  to your path 'C:\Users\YourUser\AppData\Roaming\NewEnglandcoin'
 - Restart wallet.   Fully sync the wallet to latest block. A running full node of NENG is required to allow Cheetah_Cpuminer to work.
 - Download and unpack the latest Cheetah_Cpuminer release from https://github.com/ShorelineCrypto/cheetah_cpuminer/releases
 - Double click the provided window batch file 'cheetah.bat' to start CPU mining.
 
 #### Note for Windows CPU Miners
 - Even if the wallet is fully synced under window machine, you may have to  double click the bat file,  stay for couple of minutes and then close it, and restart it again to allow cheetah to work properly.  Somehow cheetah bat file may not work with the first try. 
 
 #### Optimization for CPU solo mining with Cheetah
 - change window bat file or linux/mac sh file based on your machine CPU core number.  Recommends 2 cpu for 4 core Intel PC/Mac, 6 cpu for 8 core PC/Mac.
 For interval you may shortern it to a number such as 10, meaning the software cheetah will check full node blockchain every 10 seconds to determine to start or stop mining.
 - Example of a full command assuming 10 secondes interval and 2 core cpu in "cheetah.bat" file or "cheetah.sh" file
```
     python main.py --interval 10 --cpu 2
```



## License


Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


