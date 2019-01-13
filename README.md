# cheeta_cpuminer


## What is Cheetah_Cpuminer?

NewEnglandcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.1.2 is tested under Windows 10, Mac OSX 10.11 and Ubuntu linux 16.04.
 - Other versions of Windows, Mac or Linux platform are untested.  Cheetah under other windows (win64 ir win32), mac (OSX 10.7 or later) or linux (Debian, etc) may still work, but they are unsupported.


## Linux - Ubuntu 16.04

### How to Install Cheetah_Cpuminer

 - Under Ubuntu 16.04 based linux, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
``` 
     sudo pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run NewEnglandcoin linux wallet first (command line or QT either one). 
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
 - Optimization of CPU mining on cheetah.sh file: see below windows section for detailed recommendation. 
 
 
 ## Mac - OSX 10.11

### How to Install Cheetah_Cpuminer

 - Under OSX 10.11 based mac terminal, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
``` 
     sudo pip install python-bitcoinrpc
```

### How to Run Cheetah_Cpuminer

 - Download and run NewEnglandcoin mac wallet first (CLI or GUI either one). 
 - At the same local mac machine, using the provided newenglandcoin example file, modify rpc username password,  rename the filename  into 'newenglandcoin.conf' , run below command in mac terminal:
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
 - At the same local machine, using the provided newenglandcoin example, modify rpc username password and change the filename 
 into 'newenglandcoin.conf' ,  copy 'newenglandcoin.conf'  to your path 'C:\Users\YourUser\AppData\Roaming\NewEnglandcoin'
 - Restart wallet.   Fully sync the wallet to latest block. A running full node of NENG is required to allow Cheetah_Cpuminer to work.
 - Download and unpack the latest Cheetah_Cpuminer release from https://github.com/ShorelineCrypto/cheetah_cpuminer/releases
 - Double click the provided window batch file 'cheetah.bat' to start CPU mining.   
 - Optimization of CPU mining: change bat file based on your PC CPU core number with window wordpad.  recommends 2 cpu for 4 core Intel PC, 6 cpu for 8 core PC.  For interval you may shortern it to a number such as 60, meaning the software cheetah will check blockchain every 60 seconds to determine to start or stop mining. 
 #### Note for Windows CPU Miners
 - Even if the wallet is fully synced under window machine, you may have to  double click the bat file,  stay for couple of minutes and then close it, and restart it again to allow cheetah to work properly.  Somehow cheetah bat file may not work with the first try. 
 

## License


Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


