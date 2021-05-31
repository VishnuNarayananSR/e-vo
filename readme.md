# E-vo

An e-voting system using Blockchain

## Initial Setup:

1. Install [Ganche](https://www.trufflesuite.com/ganache) on  your system. 
  ###### Ganache is a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates.
  
2. Install the required packages by running:
```bash
pip install -r requirements.txt
```
3. Add a brownie development network by running the following command:
```bash
brownie networks add development gui host='http://127.0.0.1:7545' cmd=ganache
```
 ###### You have now told brownie that you have a blockchain network, meant for development purposes and named it gui, since it has a nice gui interface from ganache. We use this blockchain network to deploy our smart contracts from inside e-vo.

## Running the application:

```bash
cd path-to-evo/
python manage.py runserver
```

## Recompiling  Smart contracts:
###### If  you wish to make any changes to the blockchain smart contracts, you mut recompile it  after doing so. The following comand does it.
```bash
cd path-to-evo/ethereum/
brownie compile --all
```

## References:

* eth-brownie [documentation](https://readthedocs.org/projects/eth-brownie/downloads/pdf/v1.3.1_a/)
* web3.py [documentation](https://web3py.readthedocs.io/en/stable/)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.