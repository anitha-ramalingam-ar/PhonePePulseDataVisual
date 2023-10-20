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
class HoverData:
    name: str
    metric: List[Metric]


@dataclass
class Data:
    hoverDataList: List[HoverData]


@dataclass
class MapTransactionData:
    data: Data
    state_name: str
    year_with_quarter: str


def load_from_json(file_path: str, state_name: str, year_with_quarter: str) -> Optional[MapTransactionData]:
    with open(file_path, 'r') as f:
        json_data = json.load(f)

    data_obj = Data(hoverDataList=[
        HoverData(name=hover_data['name'], metric=[
            Metric(type=metric['type'], count=metric['count'], amount=metric['amount'])
            for metric in hover_data['metric']
        ])
        for hover_data in json_data['data']['hoverDataList']
    ])

    return MapTransactionData(data_obj, state_name, year_with_quarter)


def process_map_transaction_files(base_path: str):
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
                    data_list.append(data)

    return data_list
