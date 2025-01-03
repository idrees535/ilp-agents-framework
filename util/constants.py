

import configparser
import math
import os

import brownie
from brownie._config import CONFIG  # pylint: disable=no-name-in-module
#from enforce_typing import enforce_types  # pylint: disable=unused-import



from util.configutil import CONF_FILE_PATH

config = configparser.ConfigParser()
config.read(os.path.expanduser(CONF_FILE_PATH))

BROWNIE_PROJECTUniV3 = brownie.project.load("./v3_core/", name="UniV3Project1234")
#print(BROWNIE_PROJECTUniV3.available_contracts)

#if brownie.network.show_active() != "ganache":
#    brownie.network.connect("ganache")

if brownie.network.show_active() != "development":
    brownie.network.connect("development")

GOD_ACCOUNT = brownie.network.accounts[9]
RL_AGENT_ACCOUNT = brownie.network.accounts[8]

SAFETY = config["general"].getboolean("SAFETY")
assert SAFETY is not None

if not SAFETY:
    # do nothing, just return the original function
    def noop(f):
        return f

    enforce_types = noop

SILENT = config["general"].getboolean("SILENT")
assert SILENT is not None

CONFIG.argv["silent"] = SILENT  # brownie config

# big numbers

INF = math.inf
HUGEINT = 2**255  # biggest int that can be passed into contracts

# number of seconds in an hour, etc.
S_PER_MIN = 60
S_PER_HOUR = S_PER_MIN * 60
S_PER_DAY = S_PER_HOUR * 24
S_PER_WEEK = S_PER_DAY * 7
S_PER_MONTH = S_PER_DAY * 30
S_PER_YEAR = S_PER_DAY * 365

# Number of half-lives that bitcoin stops after.
# https://en.bitcoin.it/wiki/Controlled_supply#Projected_Bitcoins_Long_Term
BITCOIN_NUM_HALF_LIVES = 34

# evm stuff
GASLIMIT_DEFAULT = 5000000
BURN_ADDRESS = "0x000000000000000000000000000000000000dEaD"

OPF_ACCOUNT = brownie.network.accounts[8]
OPF_ADDRESS = OPF_ACCOUNT.address

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
