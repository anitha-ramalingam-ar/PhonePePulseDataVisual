from database.create_district_table_sql import get_district_id_by_value
from database.create_state_table_sql import get_state_id
from top.model.top_transaction_model import process_top_transaction_files


def top_transaction_state_data_conversion(cursor):
    # Step 1: Read each state top transaction json and convert as Object class
    top_transaction_data = process_top_transaction_files('extracted_file/data/top/transaction/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in top_transaction_data:

        for district in data.data.districts:
            district_id = get_district_id_by_value(cursor, district.entityName)
            if district_id is None:
                print(f"Error: District {district.entityName} not found in the database.")
                continue
            state_id = get_state_id(cursor, data.state_name)
            count = district.metric.count
            amount = district.metric.amount
            amount_str = "{:.10f}".format(amount)
            year_with_quarter = data.year_with_quarter
            query = """
                INSERT INTO TopDistrictTransactionDetails 
                (district_id, state_id, count, amount, year_with_quarter) 
                VALUES (%s, %s, %s, %s, %s);
                """
            cursor.execute(query, (district_id, state_id, count, amount_str, year_with_quarter))

        for pincode in data.data.pincodes:
            pincode_id = pincode.entityName
            if pincode_id is None:
                print(f"Error: Pincode {pincode.entityName} not found in the database.")
                continue
            state_id = get_state_id(cursor, data.state_name)
            count = pincode.metric.count
            amount = pincode.metric.amount
            amount_str = "{:.10f}".format(amount)
            year_with_quarter = data.year_with_quarter
            query = """
                INSERT INTO TopPincodeTransactionDetails 
                (pincode, state_id, count, amount, year_with_quarter) 
                VALUES (%s, %s, %s, %s, %s);
                """
            cursor.execute(query, (pincode_id, state_id, count, amount_str, year_with_quarter))
