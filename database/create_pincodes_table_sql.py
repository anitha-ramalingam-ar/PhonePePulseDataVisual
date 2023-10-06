def create_state_static_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS States (id INT AUTO_INCREMENT PRIMARY KEY,state_key VARCHAR(255) UNIQUE NOT NULL, state_value VARCHAR(255) UNIQUE NOT NULL);")
    states = {
        'andhra-pradesh': 'Andhra Pradesh',
        'arunachal-pradesh': 'Arunachal Pradesh',
        'assam': 'Assam',
        'bihar': 'Bihar',
        'chhattisgarh': 'Chhattisgarh',
        'goa': 'Goa',
        'gujarat': 'Gujarat',
        'haryana': 'Haryana',
        'himachal-pradesh': 'Himachal Pradesh',
        'jammu-&-kashmir': 'Jammu & Kashmir',
        'jharkhand': 'Jharkhand',
        'karnataka': 'Karnataka',
        'kerala': 'Kerala',
        'madhya-pradesh': 'Madhya Pradesh',
        'maharashtra': 'Maharashtra',
        'manipur': 'Manipur',
        'meghalaya': 'Meghalaya',
        'mizoram': 'Mizoram',
        'nagaland': 'Nagaland',
        'odisha': 'Odisha',
        'punjab': 'Punjab',
        'rajasthan': 'Rajasthan',
        'sikkim': 'Sikkim',
        'tamil-nadu': 'Tamil Nadu',
        'telangana': 'Telangana',
        'tripura': 'Tripura',
        'uttarakhand': 'Uttarakhand',
        'uttar-pradesh': 'Uttar Pradesh',
        'west-bengal': 'West Bengal',
        'andaman-&-nicobar-islands': 'Andaman & Nicobar Islands',
        'chandigarh': 'Chandigarh',
        'dadra-&-nagar-haveli-&-daman-&-diu': 'Dadra & Nagar Haveli & Daman & Diu',
        'lakshadweep': 'Lakshadweep',
        'delhi': 'Delhi',
        'puducherry': 'Puducherry',
        'ladakh': 'Ladakh'
    }

    for state_key, state_value in states.items():
        cursor.execute("INSERT IGNORE INTO States (state_key, state_value) VALUES (%s, %s);", (state_key, state_value))


def get_state_id(cursor, state_name):
    query = "SELECT id FROM States WHERE state_key = %s;"
    cursor.execute(query, (state_name,))
    result = cursor.fetchone()
    return result[0] if result else None
