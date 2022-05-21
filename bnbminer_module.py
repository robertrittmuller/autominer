import miners

class bnbminer(miners.miners):
    # specific settings for this miner
    projectName = 'BNB Miner'                                           # Project name
    projectCurrency = 'BNB'                                             # Currency used for this project
    loggingFilename = 'bnbminer.csv'                                    # log file name for this miner
    savefileName = 'bnbminer.status'                                    # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 2                                                      # Ratio between compounding and withdrawls (6:1 default)
    actionThreshold = 0.01                                              # reward balance that triggers an action
    currentActionCount = 0                                              # placeholder for where we are in the action counter
    contract_address = '0xce93F9827813761665CE348e33768Cb1875a9704'     # Contract address
    wallet_address = None                                               # Property for the wallet address
    private_key = None                                                  # Property for the private wallet key

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    def getCurrentReward(self):
        myPendingReward = self.minerContract.functions.getMyEggs().call({'from': self.wallet_address})
        if(myPendingReward != 0):
            return self.connection.fromWei(self.minerContract.functions.calculateEggSell(myPendingReward).call(), 'ether')
        else:
            return 0
    
    def getCurrentMiners(self):
        return self.minerContract.functions.getMyMiners().call({'from': self.wallet_address})