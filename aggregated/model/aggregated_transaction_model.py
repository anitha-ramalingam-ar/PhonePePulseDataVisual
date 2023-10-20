import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class PaymentInstrument:
    type: str
    count: int
    amount: float


@dataclass
class TransactionData:
    name: str
    paymentInstruments: List[PaymentInstrument]


@dataclass
class Data:
    transactionData: List[TransactionData]


@dataclass
class AggregatedTransactionData:
    data: Data
    state_name: str
    year_with_quarter: str


def load_from_json(file_path: str, state_name: str, year_with_quarter: str) -> AggregatedTransactionData:
    with open(file_path, 'r') as f:
        data = json.load(f)

    aggregated_data = data['data']

    transaction_data_list = []
    for td in aggregated_data['transactionData']:
        payment_instruments = [PaymentInstrument(**pi) for pi in td['paymentInstruments']]
        transaction_data_list.append(TransactionData(td['name'], payment_instruments))

    data_obj = Data(transaction_data_list)

    return AggregatedTransactionData(data_obj, state_name, year_with_quarter)


def process_aggregated_transaction_files(base_path: str):
    data_list = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.json'):
                full_path = os.path.join(root, file)

                file_name = os.path.basename(full_path)
                year = os.path.basename(os.path.dirname(full_path))
                quarter_map = {
                    "1.json": "Q1",
                    "2.json": "Q2",
                    "3.json": "Q3",
                    "4.json": "Q4"
                }
                quarter = quarter_map.get(file_name, "")

                year_with_quarter = year + " " + quarter
                state_name = os.path.basename(os.path.dirname(os.path.dirname(full_path)))

                data = load_from_json(full_path, state_name, year_with_quarter)

                if data:
                    data.state_name = state_name
                    data_list.append(data)

    return data_list
