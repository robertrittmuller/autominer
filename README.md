# Autominer Web3 Project Automation Script
BNB Miner automation script. Supports Baked Beans Miner, Grinch Bucks Miner, BNB Miner, Roast Beef, and soon several others!

## Supported Projects
<table>
<tr>
<td>
    <a href="https://bnbminer.finance?ref=0x83F85b7f200718C1E52798f90d2fBAEfd49A6671">
        <b>BNB Miner</b>
        <img src="images/bnb-miner-ico.jpg">
    </a>
</td>
<td>
    <a href="https://bakedbeans.io?ref=0x83F85b7f200718C1E52798f90d2fBAEfd49A6671">
        <b>Baked Beans Miner</b>
        <img src="images/baked-beans-ico.jpg">
</a>
</td>
</tr>
<tr>
<td>
    <a href="https://grinchbucks.com/?refer=0x83F85b7f200718C1E52798f90d2fBAEfd49A6671">
        <b>Grinch Bucks Miner</b>
        <img src="images/grinch-bucks-ico.jpg">
    </a>
</td>
<td>
    <a href="https://roastedbeef.io/#/?ref=0x83f85b7f200718c1e52798f90d2fbaefd49a6671">
        <b>Roast Beef Miner</b>
        <img src="images/roast-beef-ico.jpg">
    </a>
</td>
</tr>
<tr>
<td>
    <a href="app.solarfarm.finance/?ref=0x83F85b7f200718C1E52798f90d2fBAEfd49A6671">
        <b>Solar Farm Miner</b>
        <img src="images/solar-farm-ico.jpg">
    </a>
</td>
<td>
</td>
</tr>
</table>

## Installation
Installation is simple, just install the dependencies in your favorite Python environment, setup your wallet addresses, and run!

```
pip install -r requirements.txt
```

## Usage
This script is run at the command line and does not feature any type of graphical interface. 

### Step One - Configure your wallet addresses!

Your public wallet address and private key need to be added before the script will work. Please follow security best practices when using your private key!

```python
myWalletAddress = ""
myPrivateKey = ""
```
><i>NOTE: I HIGHLY recommend that you only set the above variables immediately before running the script, clearing them(and saving) once the script is running to avoid storing your wallet's private key on disk.</i>

### Step Two - Run the script!

```
python autominer.py
```

## Enjoy!
If you like this script, and you want to see more of these types of Web3 automation scripts, please support me by using the above project referral links! You can also check out my other work on my <a href="https://www.rittmuller.com">web site</a>.

## LICENSE
This project is distributed under the <a href="LICENSE">MIT</a> license. 
