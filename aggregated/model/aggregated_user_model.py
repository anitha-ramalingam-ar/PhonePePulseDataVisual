import os
import json
from dataclasses import dataclass
from typing import List


@dataclass
class AggregatedData:
    registeredUsers: int
    appOpens: int


@dataclass
class UserByDevice:
    brand: str
    count: int
    percentage: float


@dataclass
class Data:
    aggregated: AggregatedData
    usersByDevice: List[UserByDevice]


@dataclass
class AggregatedUserData:
    data: Data
    state_name: str
    year_with_quarter: str


def load_from_json(file_path: str, state_name: str, year_with_quarter: str) -> AggregatedUserData:
    with open(file_path, 'r') as f:
        loaded_data = json.load(f)

    if not loaded_data['data'].get('usersByDevice'):
        print(f"Skipping problematic file: {file_path}")
        return None

    aggregated_data = loaded_data['data']['aggregated']
    aggregated_obj = AggregatedData(**aggregated_data)

    users_by_device_list = [UserByDevice(**user_data) for user_data in loaded_data['data']['usersByDevice']]

    data_obj = Data(aggregated=aggregated_obj, usersByDevice=users_by_device_list)

    return AggregatedUserData(data_obj, state_name, year_with_quarter)


def process_aggregated_user_files(base_path: str):
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
