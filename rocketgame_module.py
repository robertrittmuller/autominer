import miners

class rocketgame(miners.miners):
    # specific settings for this miner
    projectName = 'Rocket Game'                                         # Project name
    projectCurrency = 'BUSD'                                            # Currency used for this project
    loggingFilename = 'rocketgame.csv'                                  # log file name for this miner
    savefileName = 'rocketgame.status'                                  # Name of file to use for saving script state in case you need to restart the script
    network = 'https://bsc-dataseed.binance.org/'                       # network API 
    contractAPI = 'https://api.bscscan.com/api'                         # contract API (needed to bet ABI)
    numActions = 6                                                      # Ratio between compounding and withdrawls (5:1 default)
    actionThreshold = 5.0                                               # reward balance that triggers an action
    currentActionCount = 0                                              # placeholder for where we are in the action counter
    contract_address = '0xe76EF9bd1BFEC3730472049D5aFF17bc9c4D3E6d'     # Contract address
    wallet_address = None                                               # Property for the wallet address
    private_key = None                                                  # Property for the private wallet key

    # sub-object properties
    connection = None                                                   # web3 connection object
    minerContract = None                                                # ABI contract object
    
    def getCurrentReward(self):
            myPendingReward = self.minerContract.functions.getMyRockets(self.wallet_address).call()
            return self.connection.fromWei(self.minerContract.functions.calculateRocketsSell(myPendingReward).call(), 'ether')
    
    def compound(self):
    # Attempt to re-bake some beans
        transaction_nonce = self.connection.eth.getTransactionCount(self.wallet_address)
        print()
        print('Processing compound transaction #', transaction_nonce)

        transaction_hash = self.minerContract.functions.hatchRockets(self.wallet_address).buildTransaction({
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

        transaction_hash = self.minerContract.functions.sellRockets().buildTransaction({
            'gas':100000,
            'gasPrice':self.connection.toWei('10','gwei'),
            'nonce': transaction_nonce
        })

        signed_transaction = self.connection.eth.account.sign_transaction(transaction_hash, private_key=self.private_key)
        self.connection.eth.send_raw_transaction(signed_transaction.rawTransaction)