from database.create_district_table_sql import get_district_id_by_value
from database.create_state_table_sql import get_state_id
from top.model.top_user_model import process_top_user_files


def top_user_state_data_conversion(cursor):
    # Step 1: Read each state top transaction json and convert as Object class
    top_user_data = process_top_user_files('extracted_file/data/top/user/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in top_user_data:

        for district in data.data.districts:
            district_id = get_district_id_by_value(cursor, district.name)
            if district_id is None:
                print(f"Error: District {district.name} not found in the database.")
                continue
            state_id = get_state_id(cursor, data.state_name)
            registered_users = district.registeredUsers
            year_with_quarter = data.year_with_quarter
            query = """
                    INSERT INTO TopDistrictUserDetails 
                    (district_id, state_id, registered_user, year_with_quarter) 
                    VALUES (%s, %s, %s, %s);
                    """
            cursor.execute(query, (district_id, state_id, registered_users, year_with_quarter))

        for pincode in data.data.pincodes:
            pincode_id = pincode.name
            if pincode_id is None:
                print(f"Error: Pincode {pincode.name} not found in the database.")
                continue
            state_id = get_state_id(cursor, data.state_name)
            registered_users = pincode.registeredUsers
            year_with_quarter = data.year_with_quarter
            query = """
                    INSERT INTO TopPincodeUserDetails 
                    (pincode, state_id, registered_user, year_with_quarter) 
                    VALUES (%s, %s, %s, %s);
                    """
            cursor.execute(query, (pincode_id, state_id, registered_users, year_with_quarter))
