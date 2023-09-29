from aggregated.service.aggregated_transaction_service import aggregated_transaction_state_data_conversion
from aggregated.service.aggregated_user_service import aggregated_user_state_data_conversion
from database.create_database_and_tables import mysql_connection, create_all_tables
from github_clone.extract_phonepe_data import clone_github_repo
from map.service.map_transaction_service import map_transaction_state_data_conversion
from map.service.map_user_service import map_user_data_conversion

repo_url = "https://github.com/PhonePe/pulse.git"
destination = "extracted_file"

if __name__ == '__main__':
    # Step 1: Clone the PhonePe GitHub repo and save that into extracted_file folder
    clone_github_repo(repo_url, destination)

    # Step 2: Create aggregated, type and state tables
    conn = mysql_connection('localhost', 3306, 'root', 'root', 'phonepe_visual')
    cursor = conn.cursor()
    create_all_tables(cursor)

    # Step 3: Proces Aggregated Transaction State Data
    aggregated_transaction_state_data_conversion(cursor)

    # Step 4: Proces Aggregated User State Data
    aggregated_user_state_data_conversion(cursor)

    # Step 5: Proces Map Transaction State Data
    map_transaction_state_data_conversion(cursor)

    # Step 6: Proces Map User State Data
    map_user_data_conversion(cursor)

    conn.commit()
    cursor.close()
    conn.close()
