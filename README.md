cheeta_cpuminer
================================


What is Cheetah_Cpuminer?
----------------

NewEnglandcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.1.0 is tested under Ubuntu linux 16.04 and under window 10
 - Other version of window platform or linux platform is untested.  Cheetah under other window (win64 ir win32) or linux (Debian, etc) may still work, but they are unsupported.


Linux - Ubuntu 16.04
===============================

How to Install Cheetah_Cpuminer
----------------

 - Under Ubuntu 16.04 based linux, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
   
     sudo pip install python-bitcoinrpc
   

How to Run Cheetah_Cpuminer 
 - Download and run NewEnglandcoin linux wallet first (command line or QT either one). 
 - At the same local linux machine, using the provided newenglandcoin example, modify rpc username password change the filename 
 into 'newenglandcoin.conf' , run below command:  
            cp newenglandcoin.conf  ~/.newenglandcoin/ 
 -  Restart wallet.   Fully sync the wallet to latest block. A full node of NENG is required to allow Cheetah_Cpuminer to work.
 - run below command using the provided the bash shell script:  
            sh cheetah.sh
 
 Window 10
===============================

How to Install Cheetah_Cpuminer
----------------
 - Download v2.7.x version of windows python from https://www.python.org/downloads/windows/ and install it.
 - Open a window command prompt terminal, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
   
     set PATH=%PATH%;C:\Python27;C:\Python27\Scripts
     pip install python-bitcoinrpc
   

How to Run Cheetah_Cpuminer 
 - Download and run NewEnglandcoin window QT wallet. 
 - At the same local machine, using the provided newenglandcoin example, modify rpc username password and change the filename 
 into 'newenglandcoin.conf' ,  copy 'newenglandcoin.conf'  to your path 'C:\Users\YourUser\AppData\Roaming\NewEnglandcoin'
 - Restart wallet.   Fully sync the wallet to latest block. A running full node of NENG is required to allow Cheetah_Cpuminer to work.
 - Download and unpack the latest Cheetah_Cpuminer release from https://github.com/ShorelineCrypto/cheetah_cpuminer/releases
 - Double click the provided window batch file 'cheetah.bat' to start CPU mining.   
 - Based on your PC CPU core number, typically 4 core PC use 3, 8 core PC use 7 to modify the command line options of window batch file 'cheetah.bat' to optimize
 your CPU mining results. 
 

License
-------

Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


