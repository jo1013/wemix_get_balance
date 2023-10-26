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
    end_block = w3.eth.block_number

    while start_block <= end_block:
        mid_block = (start_block + end_block) // 2
        mid_block_time = w3.eth.get_block(mid_block)['timestamp']

        if target_timestamp < mid_block_time:
            end_block = mid_block - 1
        elif target_timestamp > mid_block_time:
            start_block = mid_block + 1
        else:
            return mid_block
    return None



def get_balance(w3, address, token, block_number=None):
    # 체크 섬
    check_sum_address = w3.to_checksum_address(address)

    if token == 'wemix': 
        # Ether의 잔액 조회
        balance_wei = w3.eth.get_balance(check_sum_address, block_identifier=block_number)
        balance = w3.from_wei(balance_wei, 'ether')
        # 큰 수를 안전하게 처리하기 위해 문자열로 변환
        if block_number is None :
           block_number = w3.eth.block_number
        return {"balance": str(balance), "block_number" : str(block_number)}
    elif token in TokenAddresses._member_names_:
        # 토큰 컨트랙트 주소 가져오기
        token_contract_address = TokenAddresses[token].value
        # 토큰 컨트랙트 생성
        token_contract = w3.eth.contract(address=token_contract_address, abi=token_abi)
        # 잔액 조회 (가장 작은 단위)
        balance = token_contract.functions.balanceOf(check_sum_address).call(block_identifier=block_number)
        # 토큰의 decimals 값 가져오기
        decimals = token_contract.functions.decimals().call()
        # "정상" 단위로 잔액 변환
        balance_normalized = balance / (10 ** decimals)
        if block_number is None :
            block_number = w3.eth.block_number
        # 큰 수를 안전하게 처리하기 위해 문자열로 변환
        return {"balance": str(balance_normalized), "block_number" : str(block_number)}
    else:
        return {"error": "Unsupported token"}


@app.get("/balance/{address}/{token}")
async def read_balance(address: str, token: str, timestamp: str = Query(None)):
    if timestamp:
        datetime_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        target_timestamp = int(datetime_obj.timestamp())
        block_number = get_block_number_from_timestamp(target_timestamp)
    else:
        block_number = None

    return_value = get_balance(w3, address, token, block_number)
    return return_value










