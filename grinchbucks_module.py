import miners

class grinchbucks(miners.miners):
    # specific settings for this miner
    projectName = 'Grinch Bucks'                                        # Project name
    projectCurrency = 'BNB'                                             # Currency used for this project
    loggingFilename = 'grinchbucks.csv'                                 # log file name for this miner
    savefileName = 'grinchbucks.status'                                 # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 2                                                      # Ratio between compounding and withdrawls (5:1 default)
    actionThreshold = 0.005                                             # reward balance that triggers an action
    contract_address = '0xb3c0B3D3803D6C9ACf6c1af89bf1Cb728F8331B6'     # Contract address

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    def getCurrentReward(self):
        return self.connection.fromWei(self.minerContract.functions.grinchBuckRewards(self.wallet_address).call(), 'ether')