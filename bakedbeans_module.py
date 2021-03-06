import miners

class bakedbeans(miners.miners):
    # specific settings for this miner
    projectName = 'Baked Beans'                                         # Project name
    projectCurrency = 'BNB'                                             # Currency used for this project
    loggingFilename = 'bakedbeans.csv'                                  # log file name for this miner
    savefileName = 'bakedbeans.status'                                  # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 2                                                      # Ratio between compounding and withdrawls (6:1 default)
    actionThreshold = 0.005                                             # reward balance that triggers an action
    contract_address = '0xE2D26507981A4dAaaA8040bae1846C14E0Fb56bF'     # Contract address

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    def getCurrentReward(self):
        return self.connection.fromWei(self.minerContract.functions.beanRewards(self.wallet_address).call(), 'ether')