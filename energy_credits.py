# energy_credit.py
import smartpy as sp

class EnergyToken(sp.Contract):
    # Stores EnergyToken related Big Maps
    def __init__(self):
        self.init(
            energySupplied = sp.big_map(tvalue = sp.TNat),
            tokens = sp.big_map(tvalue = sp.TNat)
        ) 
    @sp.entry_point
    def supplyEnergy(self, params):
        self.data.energySupplied[sp.sender] = params.energy
        self.data.tokens[sp.sender] = params.energy

    @sp.entry_point
    def redeemTokens(self, params):
        sp.verify(self.data.tokens[sp.sender] >= params.tokens)
        self.data.tokens[sp.sender] -= params.tokens
