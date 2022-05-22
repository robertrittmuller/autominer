##################################################
## General BNB-Miner Web3 Automation Script
##################################################
## Distributed under the MIT License
##################################################
## Author: @robertrittmuller (TW: @rjrittmuller)
##################################################
from tkinter import E
from web3 import Web3
import time, json
import json
import os
import sys
import random
import csv
import datetime

# import project specific modules
import bakedbeans_module
import roastbeef_module
import grinchbucks_module
import solarfarm_module
import bnbminer_module

# Settings
intervalTime = 3600                 # time to wait between checks on the reward balance (default is once per day)
api_rate_limit = 5                  # good idea to never drop this below 5 or transactions might be blocked

try:
    #***************************************************************************
    myWalletAddress = ""            # Variable for your public wallet address
    myPrivateKey = ""               # Variable for your wallet's private key
    #***************************************************************************
except:
    print("Wallet keys not found!")
    sys.exit()

# check to make sure we have something that looks like a key pair
if(len(myWalletAddress) == 42):
    if(len(myPrivateKey) == 64):
        print("Required wallet keys loaded sucessfully!")
    else:
        print("Public key loaded, no private key found, transactions will be disabled!")
else:
    print("ERROR: Wallet keys invalid!")
    sys.exit()

# setup connnection(s) to projects
projects = []
projects.append(bakedbeans_module.bakedbeans(myWalletAddress, myPrivateKey))
time.sleep(api_rate_limit) # rate limit for API
projects.append(roastbeef_module.roastbeef(myWalletAddress, myPrivateKey))
time.sleep(api_rate_limit) # rate limit for API
projects.append(grinchbucks_module.grinchbucks(myWalletAddress, myPrivateKey))
time.sleep(api_rate_limit) # rate limit for API
projects.append(solarfarm_module.solarfarm(myWalletAddress, myPrivateKey))
time.sleep(api_rate_limit) # rate limit for API
projects.append(bnbminer_module.bnbminer(myWalletAddress, myPrivateKey))
time.sleep(api_rate_limit) # rate limit for API

print('-' * 100, 'All Contracts Loaded!')

# Setup main loop
while True:
    # Loop forever or until the contract runs out of money
    i = 0
    while i < len(projects):
        
        # define log file for this round
        csvLine = []
        errorMsg = 'None'

        print('Working on', projects[i].projectName)
    
        # Let's pull some contract / wallet data 
        myPendingReward = projects[i].getCurrentReward()
        myTotalMiners = projects[i].getCurrentMiners()

        # Important to make sure there actually is still money in the contract otherwise you incur wasted gas charges!
        minerBalance = projects[i].getContractBalance()
        print('Total Contract Balance (' + str(projects[i].projectCurrency) + ') =', minerBalance)

        print('Pending Reward (' + str(projects[i].projectCurrency) + ') =', myPendingReward)
        print('Total # of Miners =', myTotalMiners)

        action = 'None'
        if(minerBalance > 0):
            # Now we need to validate some criteria before taking any actions
            if(myPendingReward >= projects[i].actionThreshold and projects[i].getWalletBalance() > 0):
                # Now check to see what action we should do (withdraw or compound)
                print('Current action count =', projects[i].currentActionCount)
                if projects[i].currentActionCount >= projects[i].numActions: 
                    # Withdraw rewards
                    try:
                        projects[i].withdraw()
                        action = 'withdraw'
                    except Exception as e:
                        errorMsg = 'Withdraw error: ' + str(e)
                    projects[i].currentActionCount = 0
                    print('-' * 100, 'Transaction Submitted')

                else:
                    # Compound Rewards
                    try:
                        projects[i].compound()
                        action = 'compound'
                    except Exception as e:
                        errorMsg = 'Compound error: ' + str(e)
                    projects[i].currentActionCount += 1
                    print('-' * 100, 'Transaction Submitted')
        
        # save status in case we stop the script
        projects[i].saveStatus()
        print('-' * 100, '*')

        # write out the log data
        csvLine.append(datetime.datetime.now())
        csvLine.append(action)
        csvLine.append(minerBalance)
        csvLine.append(myPendingReward)
        csvLine.append(myTotalMiners)
        csvLine.append(errorMsg)
        projects[i].logTransaction(csvLine)
        csvLine = []
        
        # advance to the next project
        i += 1
        time.sleep(api_rate_limit) # rate limit for API
    
    # No wait for the specififed time
    print()
    print('Waiting for', intervalTime, 'seconds.')
    time.sleep(intervalTime)