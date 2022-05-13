import miners

class roastbeef(miners.miners):
    # specific settings for this miner
    projectName = 'Roast Beef'                                          # Project name
    projectCurrency = 'BNB'                                             # Currency used for this project
    loggingFilename = 'roastbeef.csv'                                   # log file name for this miner
    savefileName = 'roastbeef.status'                                   # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 6                                                      # Ratio between compounding and withdrawls (5:1 default)
    actionThreshold = 0.01                                              # reward balance that triggers an action
    currentActionCount = 0                                              # placeholder for where we are in the action counter
    contract_address = '0xd81F5DB384d604D85D158FCb8E00341Aff200E22'     # Contract address
    wallet_address = None                                               # Property for the wallet address
    private_key = None                                                  # Property for the private wallet key

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    def getCurrentReward(self):
        myPendingReward = self.minerContract.functions.getMyEggs().call({'from': self.wallet_address})
        return self.connection.fromWei(self.minerContract.functions.calculateEggSell(myPendingReward).call(), 'ether')

    def getCurrentMiners(self):
        return self.minerContract.functions.hatcheryMiners(self.wallet_address).call() 