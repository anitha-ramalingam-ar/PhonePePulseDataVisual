from database.create_district_table_sql import get_district_id_by_key
from database.create_state_table_sql import get_state_id
from map.model.map_transaction_model import process_map_transaction_files


def map_transaction_state_data_conversion(cursor):
    # Step 1: Read each state aggregated transaction json and convert as Object class
    map_transaction_data = process_map_transaction_files(
        'extracted_file/data/map/transaction/hover/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in map_transaction_data:
        for hover_data in data.data.hoverDataList:
            district_id = get_district_id_by_key(cursor, hover_data.name)
            if district_id is None:
                print(f"Error: District {hover_data.name} not found in the database.")
                continue
            state_id = get_state_id(cursor, data.state_name)
            count = hover_data.metric[0].count
            amount = hover_data.metric[0].amount
            amount_str = "{:.10f}".format(amount)
            year_with_quarter = data.year_with_quarter
            query = """
                INSERT INTO MapTransactionDetails 
                (district_id, state_id, count, amount, year_with_quarter) 
                VALUES (%s, %s, %s, %s, %s);
                """

            cursor.execute(query, (district_id, state_id, count, amount_str, year_with_quarter))
