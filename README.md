cheeta_cpuminer
================================


What is Cheetah_Cpuminer?
----------------

NewEnglandcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.0.0 is tested under Ubuntu linux 16.04
 - window platform is untested.  Cheetah under window operating system will be supported in next release.

How to Install Cheetah_Cpuminer
----------------

 - Under Ubuntu or Debian based linux, run below command to install python-bitcoinrpc 
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
 

License
-------

Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


