import requests

def test_1():
    block_url = 'https://blockstream.info/api/block-height/680000'
    block_info = requests.get(block_url)
    block_data = block_info.content
    block_value = block_data.decode()
    transaction_url = f'https://blockstream.info/api/block/{block_value}'
    transaction_count = requests.get(transaction_url)
    transaction_data = transaction_count.json()
    assert transaction_data['tx_count'] == 2875


def test_2():
    block_URL = 'https://blockstream.info/api/block-height/680000'
    transaction_data = requests.get(block_URL)
    transaction_info = transaction_data.content
    hash_id = transaction_info.decode()
    transaction_url = f'https://blockstream.info/api/block/{hash_id}/txs/'
    hash_data = requests.get(transaction_url)
    transaction_id = hash_data.json()
    #print(transaction_id)
    assert transaction_id.includes("96d92f03000f625a38bf8cb91c01188a02b7972238cc6c4e0c6f334cf755004d")  
           


