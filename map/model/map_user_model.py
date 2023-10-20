import json
import os
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class HoverData:
    registeredUsers: int
    appOpens: int


@dataclass
class Data:
    hoverData: Dict[str, HoverData]


@dataclass
class MapUserData:
    data: Data
    state_name: str
    year_with_quarter: str


def load_from_json(file_path: str, state_name: str, year_with_quarter: str) -> Optional[MapUserData]:
    with open(file_path, 'r') as f:
        content = f.read()

    json_data = json.loads(content)

    if not json_data.get('data') or not json_data['data'].get('hoverData'):
        return None

    hover_data_dict = json_data['data']['hoverData']

    hover_data = {key: HoverData(**value) for key, value in hover_data_dict.items()}
    data_obj = Data(hoverData=hover_data)

    return MapUserData(data_obj, state_name, year_with_quarter)


def process_map_user_files(base_path: str):
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
