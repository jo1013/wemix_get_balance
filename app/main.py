import json
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from web3 import Web3
from constants import TokenAddresses

app = FastAPI()

w3 = Web3(Web3.HTTPProvider('https://api.wemix.com/'))

# 현재 스크립트의 절대 경로를 구합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ABI_PATH = os.path.join(BASE_DIR, "resources", "token_abi.json")

with open(ABI_PATH, "r") as abi_file:
    token_abi = json.load(abi_file)


def get_block_number_from_timestamp(target_timestamp):
    # 시작 블록과 마지막 블록
    start_block = 0
    end_block = w3.eth.blockNumber

    while start_block <= end_block:
        mid_block = (start_block + end_block) // 2
        mid_block_time = w3.eth.getBlock(mid_block)['timestamp']

        if target_timestamp < mid_block_time:
            end_block = mid_block - 1
        elif target_timestamp > mid_block_time:
            start_block = mid_block + 1
        else:
            return mid_block
    return start_block if w3.eth.getBlock(start_block)['timestamp'] - target_timestamp < target_timestamp - w3.eth.getBlock(end_block)['timestamp'] else end_block


@app.get("/balance/{address}/{token}")
async def read_balance(address: str, token: str, timestamp: str = Query(None)):
    if timestamp:
        datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        target_timestamp = int(datetime_obj.timestamp())
        block_number = get_block_number_from_timestamp(target_timestamp)
    else:
        block_number = None

    if token == "eth":
        # Ether의 잔액 조회
        balance = w3.eth.get_balance(address, block_identifier=block_number)
        return {"balance": w3.from_wei(balance, 'ether')}
    elif token in TokenAddresses._member_names_:
        token_contract_address = TokenAddresses[token].value
        token_contract = w3.eth.contract(address=token_contract_address, abi=token_abi)
        balance = token_contract.functions.balanceOf(address).call(block_identifier=block_number)
        return {"balance": balance}
    else:
        raise HTTPException(status_code=400, detail="Unsupported token name")
