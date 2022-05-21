import miners

class solarfarm(miners.miners):
    # specific settings for this miner
    projectName = 'Solar Farm'                                          # Project name
    projectCurrency = 'BNB'                                             # Currency used for this project
    loggingFilename = 'solarfarm.csv'                                   # log file name for this miner
    savefileName = 'solarfarm.status'                                   # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 10                                                     # Ratio between compounding and withdrawls (6:1 default)
    actionThreshold = 0.005                                             # reward balance that triggers an action
    currentActionCount = 0                                              # placeholder for where we are in the action counter
    contract_address = '0x7fE8bb9D90Cd3e4Cf89B0e539cD0542b3B779c2c'     # Contract address
    wallet_address = None                                               # Property for the wallet address
    private_key = None                                                  # Property for the private wallet key

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object

    def getCurrentReward(self):
        return self.connection.fromWei(self.minerContract.functions.beanRewards(self.wallet_address).call(), 'ether')