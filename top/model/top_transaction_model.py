import json
import os
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Metric:
    type: str
    count: int
    amount: float


@dataclass
class Entity:
    entityName: str
    metric: Metric


@dataclass
class Data:
    states: Optional[str]  # states field was null in the JSON; hence, it's Optional
    districts: List[Entity]
    pincodes: List[Entity]


@dataclass
class TopTransactionData:
    data: Data
    state_name: str
    year_with_quarter: str


def load_from_json(file_path: str, state_name: str, year_with_quarter: str) -> TopTransactionData:
    with open(file_path, 'r') as f:
        data = json.load(f)

    districts = [Entity(entityName=d['entityName'], metric=Metric(**d['metric'])) for d in data['data']['districts']]
    pincodes = [Entity(entityName=p['entityName'], metric=Metric(**p['metric'])) for p in data['data']['pincodes']]
    data_obj = Data(states=data['data']['states'], districts=districts, pincodes=pincodes)

    return TopTransactionData(data_obj, state_name, year_with_quarter)


def process_top_transaction_files(base_path: str):
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
