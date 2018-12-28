cheeta_cpuminer
================================


What is Cheetah_Cpuminer?
----------------

NewEnglandcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks 
 
 - v1.0.0 is testest under Ubuntu linux 16.04
 - window platforum is untested.  Window platforum will be supported in next release

How to Install Cheetah_Cpuminer
----------------

 - Under Ubuntu or Debian based linux, run below command to install python-bitcoinrpc 
   ( https://github.com/jgarzik/python-bitcoinrpc )
     pip install python-bitcoinrpc


How to Run Cheetah_Cpuminer
 - Download and run NewEnglandcoin linux wallet first (command line or QT either one)
 - At the same local linux machine, modify the provided newenglandcoin example, change the filename 
 into 'newenglandcoin.conf' , run below command:  cp newenglandcoin.conf  ~/.newenglandcoin/
 - run below command using the provided the bash shell script:  sh cheetah.sh
 

License
-------

Cheetah_Cpuminer is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


