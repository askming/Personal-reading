# [Mastering Bitcoin](https://github.com/askming/Personal-reading/issues/2)

## Constructing a transaction

## Bitcoin mining
- The mining process serves two purposes in bitcoin:
  - Mining creates new bitcoins in each block, almost like a central bank printing new money. 
  - Mining creates trust by ensuring that transactions are only confirmed if enough computational power was devoted to the block that contains them.

---

*2021-07-25*

### Chapter 3. The Bitcoin Client

- Reference client: _Bitcoin Core_, also known as the "Satoshi Client". bitcoin.org
  - It implements all aspects of the bitcoin system, including wallets, a transaction verification engine with a full copy of the entire transaction ledger (blockchain), and full network node in the peer-to-peer bitcoin network.
- Once you have completed installation you should have a new application called Bitcoin-Qt in your application list.
  - The first time you run Bitcoin Core it will start downloading the blockchain, a process that might take several days
  - > Bitcoin Core keeps a full copy of the transaction ledger (blockchain), with every transaction that has ever occurred on the bitcoin network since its inception in 2009. This dataset is several gigabytes in size (approximately 16 GB in late 2013) and is downloaded incrementally over several days. The client will not be able to process transactions or update account balances until the full blockchain dataset is downloaded. During that time, the client will display “out of sync” next to the account balances and show “Synchronizing” in the footer. Make sure you have enough disk space, bandwidth, and time to complete the initial synchronization.
- For developers, there is also the option to download the full source code as a ZIP archive or by cloning the authoritative source repository from GitHub.
  - suffix "rc" in version/tag numbers means release candidate
  - The command-line bitcoin client is also known as `bitcoind` on Linux.
  - Steps to install bitcoin from command-line (autogen/configure/make system)
    - `autogen` creates a set of automatic configuration scripts that will interrogate your system to discover the correct settings and ensure you have all the necessary libraries to compile the code.
    - the `configure` command will create the customized build scripts that will allow us to compile bitcoind.
    - use `make` to compile the software
    - last step is to install using `make install`
    - The default installation of bitcoind puts it in `/usr/local/bin`. 
    ```
    git checkout vxx.xx
    ./autogen.sh
    ./configure
    make
    sudo make install
    ```
- When you first run bitcoind, it will remind you to create a configuration file with a strong password for the JSON-RPC interface. 
  - Create a file inside the .bitcoin directory so that it is named .bitcoin/bitcoin.conf and enter a username and password
  - The first time you run it, it will rebuild the bitcoin blockchain by downloading all the blocks. This is a multigigabyte file and will take an average of two days to download in full. You can shorten the blockchain initialization time by downloading a partial copy of the blockchain using a BitTorrent client from SourceForge.
  - Run bitcoind in the background with the option `-daemon`: `$ bitcoind -daemon`
- The Bitcoin Core client implements a JSON-RPC interface that can also be accessed using the command-line helper bitcoin-cli. The command line allows us to experiment interactively with the capabilities that are also available programmatically via the API.
  - invoke the help command to see a list of the available bitcoin RPC commands: `$ bitcoin-cli help`