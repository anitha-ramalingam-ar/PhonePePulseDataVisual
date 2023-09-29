from aggregated.model.aggregated_transaction_model import process_aggregated_transaction_files
from aggregated.sql.aggregated_transaction_sql import get_transaction_type_id
from database.create_state_table_sql import get_state_id


def aggregated_transaction_state_data_conversion(cursor):
    # Step 1: Read each state aggregated transaction json and convert as Object class
    aggregated_transaction_data = process_aggregated_transaction_files(
        'extracted_file/data/aggregated/transaction/country/india/state')

    # Step 2: Convert JSON to Object and insert each state with quarter record into table
    for data in aggregated_transaction_data:
        transaction_type_id = get_transaction_type_id(cursor, data.data.transactionData[0].name)
        state_id = get_state_id(cursor, data.state_name)
        instrument_type = data.data.transactionData[0].paymentInstruments[0].type
        count = data.data.transactionData[0].paymentInstruments[0].count
        amount = data.data.transactionData[0].paymentInstruments[0].amount
        amount_str = "{:.10f}".format(amount)
        year_with_quarter = data.year_with_quarter
        query = """
            INSERT INTO AggregatedTransactionDetails 
            (transaction_type_id, state_id, instrument_type, count, amount, year_with_quarter) 
            VALUES (%s, %s, %s, %s, %s, %s);
            """

        cursor.execute(query, (transaction_type_id, state_id, instrument_type, count, amount_str, year_with_quarter))
