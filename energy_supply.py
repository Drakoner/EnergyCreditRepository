# supply_energy.py
import sqlite3
from pytezos import pytezos
from energy_token import EnergyToken

def read_energy_meter(supplier):
    # This function should read the energy meter of the supplier and return the energy supplied.
    # Need to figure out signal and signatue from meter readings and integration with python. Maybe Physical -> Digital -> Rust -> Python -> Tezos? NO STUPID IDEA
    pass



def supply_energy(contract_address):
    # Connect to the SQLite database
    conn = sqlite3.connect('suppliers.db')
    cursor = conn.cursor()

    # Query the database for suppliers and their keys
    cursor.execute("SELECT supplier, key FROM suppliers")
    suppliers = cursor.fetchall()

    for supplier, key in suppliers:
        energy = read_energy_meter(supplier)
        pytezos.using(key=key).contract(contract_address).supplyEnergy(energy).inject()

    # Close the connection to the database
    conn.close()

# Using test contract address for demonstration
contract_address = 'tz2G5RTxrjdZmPEj4thinTLq2tQDkkiwPGev'
supply_energy(contract_address)

def mint_energy_credits(contract_address):
    # Connect to the SQLite database
    conn = sqlite3.connect('suppliers.db')
    cursor = conn.cursor()

    # Initialize a counter for new energy credits
    new_credits = 0

    # Query the database for suppliers and their keys
    cursor.execute("SELECT supplier, key FROM suppliers")
    suppliers = cursor.fetchall()

    for supplier, key in suppliers:
        energy = read_energy_meter(supplier)
        result = pytezos.using(key=key).contract(contract_address).supplyEnergy(energy).inject()
        
        # If the transaction was successful, increment the counter and add energy credits to supplier's wallet
        if result['status'] == 'applied':
            new_credits += energy
            # Add energy credits to the supplier's wallet
            EnergyToken(contract_address).mint(supplier, energy)

        else:
            print(f"Transaction failed for suplier {supplier}")


    # Close the connection to the database
    conn.close()

    # Return the number of new energy credits
    return new_credits

# Call the function and store the result
new_credits = mint_energy_credits(contract_address)

# Write the result to energy_monitor.py
with open('energy_monitor.py', 'w') as file:
    file.write(f'new_credits = {new_credits}\n')

# Calll the sql database to get the energy producer address
def get_supplier_details():
    # Connect to the SQLite database
    conn = sqlite3.connect('suppliers.db')
    cursor = conn.cursor()

    # Query the database for suppliers, their keys and their wallet addresses
    cursor.execute("SELECT supplier, key, wallet_address, amount FROM suppliers")
    supplier_details = cursor.fetchall()

    # Close the connection to the database
    conn.close()

    # Return the supplier details
    return supplier_details

# Call the function and store the result
supplier_details = get_supplier_details()

# Print the supplier details
for detail in supplier_details:
    print(f'Supplier: {detail[0]}, Key: {detail[1]}, Wallet Address: {detail[2]}, Amount: {detail[3]}')