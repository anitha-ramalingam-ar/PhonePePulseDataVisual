def create_aggregated_transaction_type_static_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS TransactionTypes (id INT AUTO_INCREMENT PRIMARY KEY,types VARCHAR(255) UNIQUE NOT NULL);")
    transaction_types = {
        'Recharge & bill payments',
        'Peer-to-peer payments',
        'Merchant payments',
        'Financial Services',
        'Others'
    }

    for transaction_type in transaction_types:
        cursor.execute("INSERT IGNORE INTO TransactionTypes (types) VALUES (%s);", (transaction_type,))


def create_aggregated_transaction_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AggregatedTransactionDetails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        transaction_type_id INT NOT NULL,
        state_id INT NOT NULL,
        instrument_type VARCHAR(255) NOT NULL,
        count BIGINT NOT NULL,
        amount DECIMAL(30,10) NOT NULL, 
        year_with_quarter VARCHAR(255) NOT NULL,
        FOREIGN KEY (transaction_type_id) REFERENCES TransactionTypes(id),
        FOREIGN KEY (state_id) REFERENCES States(id));
    """)


def get_transaction_type_id(cursor, transaction_type_name):
    query = "SELECT id FROM TransactionTypes WHERE types = %s;"
    cursor.execute(query, (transaction_type_name,))
    result = cursor.fetchone()
    return result[0] if result else None
