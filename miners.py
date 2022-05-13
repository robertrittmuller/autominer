from web3 import Web3
from os.path import exists
import json
import requests
import csv

class miners(object):
    # specific settings for this miner
    projectName = ''                                                    # Project name
    projectCurrency = ''                                                # Currency used for this project
    loggingFilename = ''                                                # log file name for this miner
    savefileName = ''                                                   # Name of file to use for saving script state in case you need to restart the script
    network = ''                                                        # network API 
    contractAPI = ''                                                    # contract API (needed to bet ABI)
    numActions = 5                                                      # Ratio between compounding and withdrawls
    actionThreshold = 0.01                                              # reward balance that triggers an action
    currentActionCount = 1                                              # placeholder for where we are in the action counter
    contract_address = ''                                               # Contract address
    wallet_address = None                                               # Property for the wallet address
    private_key = None                                                  # Property for the private wallet key

    # sub-object properties
    isConnected = False                                                 # boolean for connection status
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    # Basic core functions
    def __init__(self, wallet_address, private_key):
        self.connection = Web3(Web3.HTTPProvider(self.network))
        self.isConnected = self.connection.isConnected()
        self.wallet_address = wallet_address
        self.private_key = private_key

        # Load saved status if it exists
        self.getSavedStatus()

        # setup contract
        self.setupContract()
        print('Contract loaded for', str(self.projectName))
    
    def setWalletAddress(self, wallet_address):
            self.wallet_address = wallet_address

    def getWalletBalance(self):
        balance = self.connection.eth.get_balance(self.wallet_address)
        return self.connection.fromWei(balance,'ether')
    
    def getContractBalance(self):
        minerBalance = self.minerContract.functions.getBalance().call()
        return self.connection.fromWei(minerBalance, 'ether')
    
    def getJSONABI(self):
        API_ENDPOINT = self.contractAPI+'?module=contract&action=getabi&address='+str(self.contract_address)
        r = requests.get(url = API_ENDPOINT)
        response = r.json()
        return json.loads(response['result'])

    def setupContract(self):
        json_abi = self.getJSONABI()
        self.minerContract = self.connection.eth.contract(address=self.contract_address, abi=json_abi)

    def logTransaction(self, logline):
        # setup logging
        logfile = open(self.loggingFilename, "a")
        csvfile = csv.writer(logfile)

        # log to csv
        csvfile.writerow(logline)
        logfile.flush()
        logfile.close()
    
    def saveStatus(self):
        savefile = open(self.savefileName, "w")
        savefile.write(str(self.currentActionCount))
        savefile.close()

    def getSavedStatus(self):
        if exists(self.savefileName):
            savefile = open(self.savefileName, "r")
            status = savefile.read()
            self.currentActionCount = int(status)
            savefile.close()
        else:
            self.saveStatus()

    def getCurrentMiners(self):
        return self.minerContract.functions.getMyMiners(self.wallet_address).call() 

    # primary functions
    def compound(self):
    # Attempt to re-bake some beans
        transaction_nonce = self.connection.eth.getTransactionCount(self.wallet_address)
        print()
        print('Processing compound transaction #', transaction_nonce)

        transaction_hash = self.minerContract.functions.hatchEggs(self.wallet_address).buildTransaction({
            'gas':100000,
            'gasPrice':self.connection.toWei('10','gwei'),
            'nonce': transaction_nonce
    })

        signed_transaction = self.connection.eth.account.sign_transaction(transaction_hash, private_key=self.private_key)
        self.connection.eth.send_raw_transaction(signed_transaction.rawTransaction)

    def withdraw(self):
        # Attempt to eat some beans (withdraw from contract)
        transaction_nonce = self.connection.eth.getTransactionCount(self.wallet_address)
        print()
        print('Processing contract withdrawl transaction #', transaction_nonce)

        transaction_hash = self.minerContract.functions.sellEggs().buildTransaction({
            'gas':100000,
            'gasPrice':self.connection.toWei('10','gwei'),
            'nonce': transaction_nonce
        })

        signed_transaction = self.connection.eth.account.sign_transaction(transaction_hash, private_key=self.private_key)
        self.connection.eth.send_raw_transaction(signed_transaction.rawTransaction)