def create_district_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Districts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state_id INT,
            district_key VARCHAR(255) UNIQUE NOT NULL,
            district_value VARCHAR(255) UNIQUE NOT NULL,
            FOREIGN KEY (state_id) REFERENCES States(id)
        );
    """)


def insert_district_values(cursor, state_key, districts):
    cursor.execute("SELECT id FROM States WHERE state_key = %s;", (state_key,))
    state_id = cursor.fetchone()[0]

    for district_key, district_value in districts.items():
        cursor.execute("INSERT IGNORE INTO Districts (state_id, district_key, district_value) VALUES (%s, %s, %s);",
                       (state_id, district_key, district_value))


districts_of_andhra_pradesh = {
    'east godavari district': 'East Godavari', 'srikakulam district': 'Srikakulam',
    'spsr nellore district': 'Spsr Nellore', 'vizianagaram district': 'Vizianagaram',
    'visakhapatnam district': 'Visakhapatnam', 'prakasam district': 'Prakasam', 'anantapur district': 'Anantapur',
    'ysr district': 'Ysr', 'west godavari district': 'West Godavari', 'kurnool district': 'Kurnool',
    'chittoor district': 'Chittoor', 'guntur district': 'Guntur', 'krishna district': 'Krishna',
}

districts_of_arunachal_pradesh = {
    "Lower Dibang Valley District": "Lower Dibang Valley",
    "Lower Subansiri District": "Lower Subansiri",
    "Longding District": "Longding",
    "West Siang District": "West Siang",
    "Kamle District": "Kamle",
    "Upper Siang District": "Upper Siang",
    "Tirap District": "Tirap",
    "Papum Pare District": "Papum Pare",
    "Kurung Kumey District": "Kurung Kumey",
    "Anjaw District": "Anjaw",
    "Siang District": "Siang",
    "Lower Siang District": "Lower Siang",
    "Kra Daadi District": "Kra Daadi",
    "Changlang District": "Changlang",
    "Pakke Kessang District": "Pakke Kessang",
    "Dibang Valley District": "Dibang Valley",
    "West Kameng District": "West Kameng",
    "Shi Yomi District": "Shi Yomi",
    "East Siang District": "East Siang",
    "Upper Subansiri District": "Upper Subansiri",
    "East Kameng District": "East Kameng",
    "Lohit District": "Lohit",
    "Lepa Rada District": "Lepa Rada",
    "Tawang District": "Tawang",
    "Namsai District": "Namsai"
}

districts_of_assam = {
    'tinsukia district': 'Tinsukia', 'lakhimpur district': 'Lakhimpur', 'kamrup district': 'Kamrup',
    'kokrajhar district': 'Kokrajhar', 'karbi anglong district': 'Karbi Anglong', 'sivasagar district': 'Sivasagar',
    'dibrugarh district': 'Dibrugarh', 'south salmara mancachar district': 'South Salmara Mancachar',
    'nagaon district': 'Nagaon', 'dhubri district': 'Dhubri', 'golaghat district': 'Golaghat',
    'udalguri district': 'Udalguri', 'majuli district': 'Majuli', 'sonitpur district': 'Sonitpur',
    'hojai district': 'Hojai', 'marigaon district': 'Marigaon', 'chirang district': 'Chirang',
    'cachar district': 'Cachar', 'nalbari district': 'Nalbari', 'west karbi anglong district': 'West Karbi Anglong',
    'dhemaji district': 'Dhemaji', 'karimganj district': 'Karimganj', 'bongaigaon district': 'Bongaigaon',
    'dima hasao district': 'Dima Hasao', 'baksa district': 'Baksa', 'charaideo district': 'Charaideo',
    'darrang district': 'Darrang', 'kamrup metropolitan district': 'Kamrup Metropolitan',
    'hailakandi district': 'Hailakandi', 'barpeta district': 'Barpeta', 'goalpara district': 'Goalpara',
    'biswanath district': 'Biswanath', 'jorhat district': 'Jorhat',
}

districts_of_bihar = {
    'madhepura district': 'Madhepura', 'purnia district': 'Purnia', 'nalanda district': 'Nalanda',
    'buxar district': 'Buxar', 'darbhanga district': 'Darbhanga', 'nawada district': 'Nawada',
    'jamui district': 'Jamui', 'sheikhpura district': 'Sheikhpura', 'siwan district': 'Siwan',
    'muzaffarpur district': 'Muzaffarpur', 'patna district': 'Patna', 'jehanabad district': 'Jehanabad',
    'rohtas district': 'Rohtas', 'begusarai district': 'Begusarai', 'supaul district': 'Supaul',
    'sitamarhi district': 'Sitamarhi', 'saran district': 'Saran', 'arwal district': 'Arwal',
    'vaishali district': 'Vaishali', 'pashchim champaran district': 'Pashchim Champaran',
    'gopalganj district': 'Gopalganj', 'lakhisarai district': 'Lakhisarai', 'aurangabad district': 'Aurangabad',
    'kaimur bhabua district': 'Kaimur Bhabua', 'araria district': 'Araria', 'munger district': 'Munger',
    'katihar district': 'Katihar', 'khagaria district': 'Khagaria', 'saharsa district': 'Saharsa',
    'bhagalpur district': 'Bhagalpur', 'madhubani district': 'Madhubani', 'kishanganj district': 'Kishanganj',
    'gaya district': 'Gaya', 'samastipur district': 'Samastipur', 'banka district': 'Banka',
    'purbi champaran district': 'Purbi Champaran', 'sheohar district': 'Sheohar', 'bhojpur district': 'Bhojpur',
}

districts_of_chandigarh = {
    'chandigarh district': 'Chandigarh'
}

districts_of_chhattisgarh = {
    'dhamtari district': 'Dhamtari', 'korba district': 'Korba', 'surajpur district': 'Surajpur',
    'baloda bazar district': 'Baloda Bazar', 'sukma district': 'Sukma', 'raigarh district': 'Raigarh',
    'janjgir champa district': 'Janjgir Champa', 'jashpur district': 'Jashpur', 'balod district': 'Balod',
    'kabirdham district': 'Kabirdham', 'surguja district': 'Surguja', 'dantewada district': 'Dantewada',
    'gariyaband district': 'Gariyaband', 'durg district': 'Durg', 'rajnandgaon district': 'Rajnandgaon',
    'raipur district': 'Raipur', 'narayanpur district': 'Narayanpur', 'kanker district': 'Kanker',
    'korea district': 'Korea', 'mungeli district': 'Mungeli', 'bilaspur district': 'Bilaspur',
    'balrampur district': 'Balrampur', 'bijapur district': 'Bijapur', 'bemetara district': 'Bemetara',
    'bastar district': 'Bastar', 'kondagaon district': 'Kondagaon', 'mahasamund district': 'Mahasamund',
}

districts_of_goa = {
    'north goa district': 'North Goa', 'south goa district': 'South Goa',
}

districts_of_gujarat = {
    'anand district': 'Anand', 'jamnagar district': 'Jamnagar', 'devbhumi dwarka district': 'Devbhumi Dwarka',
    'rajkot district': 'Rajkot', 'aravallis district': 'Aravallis', 'chhotaudepur district': 'Chhotaudepur',
    'botad district': 'Botad', 'bharuch district': 'Bharuch', 'bhavnagar district': 'Bhavnagar',
    'junagadh district': 'Junagadh', 'mahesana district': 'Mahesana', 'the dangs district': 'The Dangs',
    'kheda district': 'Kheda', 'surat district': 'Surat', 'porbandar district': 'Porbandar',
    'gandhinagar district': 'Gandhinagar', 'panch mahals district': 'Panch Mahals', 'narmada district': 'Narmada',
    'gir somnath district': 'Gir Somnath', 'valsad district': 'Valsad', 'mahisagar district': 'Mahisagar',
    'sabar kantha district': 'Sabar Kantha', 'tapi district': 'Tapi', 'vadodara district': 'Vadodara',
    'banas kantha district': 'Banas Kantha', 'amreli district': 'Amreli', 'ahmadabad district': 'Ahmadabad',
    'dohad district': 'Dohad', 'navsari district': 'Navsari', 'patan district': 'Patan', 'kachchh district': 'Kachchh',
    'surendranagar district': 'Surendranagar', 'morbi district': 'Morbi',
}

districts_of_haryana = {
    'yamunanagar district': 'Yamunanagar', 'sonipat district': 'Sonipat', 'jind district': 'Jind',
    'rohtak district': 'Rohtak', 'faridabad district': 'Faridabad', 'mahendragarh district': 'Mahendragarh',
    'hisar district': 'Hisar', 'karnal district': 'Karnal', 'fatehabad district': 'Fatehabad',
    'palwal district': 'Palwal', 'charkhi dadri district': 'Charkhi Dadri', 'ambala district': 'Ambala',
    'rewari district': 'Rewari', 'panchkula district': 'Panchkula', 'bhiwani district': 'Bhiwani',
    'sirsa district': 'Sirsa', 'mewat district': 'Mewat', 'panipat district': 'Panipat',
    'gurugram district': 'Gurugram', 'kaithal district': 'Kaithal', 'kurukshetra district': 'Kurukshetra',
    'jhajjar district': 'Jhajjar'
}

districts_of_himachal_pradesh = {
    'solan district': 'Solan', 'sirmaur district': 'Sirmaur', 'shimla district': 'Shimla',
    'bilaspur district': 'Bilaspur', 'hamirpur district': 'Hamirpur', 'una district': 'Una',
    'kangra district': 'Kangra', 'kullu district': 'Kullu', 'mandi district': 'Mandi',
    'lahul and spiti district': 'Lahul And Spiti', 'chamba district': 'Chamba', 'kinnaur district': 'Kinnaur',
}

districts_of_jammu_kashmir = {
    'muzaffarabad district': 'Muzaffarabad', 'doda district': 'Doda', 'samba district': 'Samba',
    'mirpur district': 'Mirpur', 'srinagar district': 'Srinagar', 'baramulla district': 'Baramulla',
    'jammu district': 'Jammu', 'ganderbal district': 'Ganderbal', 'udhampur district': 'Udhampur',
    'bandipore district': 'Bandipore', 'reasi district': 'Reasi', 'shopian district': 'Shopian',
    'poonch district': 'Poonch', 'kathua district': 'Kathua', 'kishtwar district': 'Kishtwar',
    'pulwama district': 'Pulwama', 'ramban district': 'Ramban', 'rajouri district': 'Rajouri',
    'kulgam district': 'Kulgam', 'budgam district': 'Budgam', 'anantnag district': 'Anantnag',
    'kupwara district': 'Kupwara',
}

districts_of_jharkhand = {
    'ramgarh district': 'Ramgarh', 'ranchi district': 'Ranchi', 'east singhbhum district': 'East Singhbhum',
    'jamtara district': 'Jamtara', 'dumka district': 'Dumka', 'koderma district': 'Koderma',
    'hazaribagh district': 'Hazaribagh', 'simdega district': 'Simdega', 'garhwa district': 'Garhwa',
    'saraikela kharsawan district': 'Saraikela Kharsawan', 'gumla district': 'Gumla', 'chatra district': 'Chatra',
    'khunti district': 'Khunti', 'dhanbad district': 'Dhanbad', 'godda district': 'Godda',
    'deoghar district': 'Deoghar', 'palamu district': 'Palamu', 'latehar district': 'Latehar',
    'west singhbhum district': 'West Singhbhum', 'pakur district': 'Pakur', 'lohardaga district': 'Lohardaga',
    'sahebganj district': 'Sahebganj', 'giridih district': 'Giridih', 'bokaro district': 'Bokaro',
}

districts_of_karnataka = {
    'mysuru district': 'Mysuru', 'chitradurga district': 'Chitradurga', 'kalaburagi district': 'Kalaburagi',
    'ramanagara district': 'Ramanagara', 'mandya district': 'Mandya', 'kodagu district': 'Kodagu',
    'chikkamagaluru district': 'Chikkamagaluru', 'haveri district': 'Haveri', 'ballari district': 'Ballari',
    'belagavi district': 'Belagavi', 'kolar district': 'Kolar', 'uttara kannada district': 'Uttara Kannada',
    'tumakuru district': 'Tumakuru', 'yadgir district': 'Yadgir', 'bengaluru urban district': 'Bengaluru Urban',
    'chikkaballapura district': 'Chikkaballapura', 'davanagere district': 'Davanagere',
    'bagalkote district': 'Bagalkote', 'vijayapura district': 'Vijayapura', 'koppal district': 'Koppal',
    'bidar district': 'Bidar', 'bengaluru rural district': 'Bengaluru Rural', 'raichur district': 'Raichur',
    'chamarajanagara district': 'Chamarajanagara', 'dakshina kannada district': 'Dakshina Kannada',
    'hassan district': 'Hassan', 'dharwad district': 'Dharwad', 'shivamogga district': 'Shivamogga',
    'udupi district': 'Udupi', 'gadag district': 'Gadag',
}

districts_of_kerala = {
    'thiruvananthapuram district': 'Thiruvananthapuram', 'kasaragod district': 'Kasaragod',
    'malappuram district': 'Malappuram', 'pathanamthitta district': 'Pathanamthitta', 'wayanad district': 'Wayanad',
    'alappuzha district': 'Alappuzha', 'kozhikode district': 'Kozhikode', 'kollam district': 'Kollam',
    'thrissur district': 'Thrissur', 'palakkad district': 'Palakkad', 'kannur district': 'Kannur',
    'kottayam district': 'Kottayam', 'ernakulam district': 'Ernakulam', 'idukki district': 'Idukki'
}

districts_of_madhya_pradesh = {
    'morena district': 'Morena', 'alirajpur district': 'Alirajpur', 'sehore district': 'Sehore',
    'rajgarh district': 'Rajgarh', 'khargone district': 'Khargone', 'satna district': 'Satna',
    'narsinghpur district': 'Narsinghpur', 'jabalpur district': 'Jabalpur', 'hoshangabad district': 'Hoshangabad',
    'vidisha district': 'Vidisha', 'balaghat district': 'Balaghat', 'singrauli district': 'Singrauli',
    'betul district': 'Betul', 'sidhi district': 'Sidhi', 'datia district': 'Datia', 'dewas district': 'Dewas',
    'sheopur district': 'Sheopur', 'neemuch district': 'Neemuch', 'raisen district': 'Raisen',
    'mandsaur district': 'Mandsaur', 'barwani district': 'Barwani', 'katni district': 'Katni',
    'dindori district': 'Dindori', 'shivpuri district': 'Shivpuri', 'gwalior district': 'Gwalior',
    'anuppur district': 'Anuppur', 'agar malwa district': 'Agar Malwa', 'ashoknagar district': 'Ashoknagar',
    'sagar district': 'Sagar', 'niwari district': 'Niwari', 'rewa district': 'Rewa', 'shajapur district': 'Shajapur',
    'ujjain district': 'Ujjain', 'bhind district': 'Bhind', 'tikamgarh district': 'Tikamgarh',
    'seoni district': 'Seoni', 'harda district': 'Harda', 'burhanpur district': 'Burhanpur', 'damoh district': 'Damoh',
    'bhopal district': 'Bhopal', 'jhabua district': 'Jhabua', 'dhar district': 'Dhar', 'guna district': 'Guna',
    'east nimar district': 'East Nimar', 'chhindwara district': 'Chhindwara', 'umaria district': 'Umaria',
    'mandla district': 'Mandla', 'indore district': 'Indore', 'shahdol district': 'Shahdol',
    'ratlam district': 'Ratlam', 'panna district': 'Panna', 'chhatarpur district': 'Chhatarpur'
}

districts_of_maharashtra = {
    'jalgaon district': 'Jalgaon',
    'latur district': 'Latur',
    'thane district': 'Thane',
    'bhandara district': 'Bhandara',
    'nandurbar district': 'Nandurbar',
    'chandrapur district': 'Chandrapur',
    'kolhapur district': 'Kolhapur',
    'solapur district': 'Solapur',
    'mumbai district': 'Mumbai',
    'sindhudurg district': 'Sindhudurg',
    'dhule district': 'Dhule',
    'wardha district': 'Wardha',
    'parbhani district': 'Parbhani',
    'mumbai suburban district': 'Mumbai Suburban',
    'hingoli district': 'Hingoli',
    'ratnagiri district': 'Ratnagiri',
    'nanded district': 'Nanded',
    'osmanabad district': 'Osmanabad',
    'nagpur district': 'Nagpur',
    'buldhana district': 'Buldhana',
    'nashik district': 'Nashik',
    'akola district': 'Akola',
    'yavatmal district': 'Yavatmal',
    'aurangabad district': 'Aurangabad',
    'amravati district': 'Amravati',
    'washim district': 'Washim',
    'sangli district': 'Sangli',
    'gadchiroli district': 'Gadchiroli',
    'raigad district': 'Raigad',
    'palghar district': 'Palghar',
    'jalna district': 'Jalna',
    'gondia district': 'Gondia',
    'ahmednagar district': 'Ahmednagar',
    'pune district': 'Pune',
    'beed district': 'Beed',
    'satara district': 'Satara', }

districts_of_manipur = {
    'kangpokpi district': 'Kangpokpi',
    'noney district': 'Noney',
    'imphal east district': 'Imphal East',
    'thoubal district': 'Thoubal',
    'kakching district': 'Kakching',
    'jiribam district': 'Jiribam',
    'ukhrul district': 'Ukhrul',
    'tamenglong district': 'Tamenglong',
    'kamjong district': 'Kamjong',
    'chandel district': 'Chandel',
    'bishnupur district': 'Bishnupur',
    'senapati district': 'Senapati',
    'pherzawl district': 'Pherzawl',
    'churachandpur district': 'Churachandpur',
    'tengnoupal district': 'Tengnoupal',
    'imphal west district': 'Imphal West',
}

districts_of_meghalaya = {
    'north garo hills district': 'North Garo Hills',
    'south west khasi hills district': 'South West Khasi Hills',
    'west garo hills district': 'West Garo Hills',
    'south garo hills district': 'South Garo Hills',
    'east jaintia hills district': 'East Jaintia Hills',
    'south west garo hills district': 'South West Garo Hills',
    'east khasi hills district': 'East Khasi Hills',
    'east garo hills district': 'East Garo Hills',
    'ribhoi district': 'Ribhoi',
    'west jaintia hills district': 'West Jaintia Hills',
    'west khasi hills district': 'West Khasi Hills'
}

districts_of_mizoram = {
    'serchhip district': 'Serchhip',
    'aizawl district': 'Aizawl',
    'lunglei district': 'Lunglei',
    'mamit district': 'Mamit',
    'lawngtlai district': 'Lawngtlai',
    'kolasib district': 'Kolasib',
    'champhai district': 'Champhai',
    'saiha district': 'Saiha'
}

districts_of_nagaland = {
    'mon district': 'Mon',
    'phek district': 'Phek',
    'longleng district': 'Longleng',
    'mokokchung district': 'Mokokchung',
    'kiphire district': 'Kiphire',
    'kohima district': 'Kohima',
    'tuensang district': 'Tuensang',
    'peren district': 'Peren',
    'dimapur district': 'Dimapur',
    'zunheboto district': 'Zunheboto',
    'wokha district': 'Wokha'
}

districts_of_odisha = {
    'rayagada district': 'Rayagada',
    'koraput district': 'Koraput',
    'malkangiri district': 'Malkangiri',
    'sambalpur district': 'Sambalpur',
    'kalahandi district': 'Kalahandi',
    'anugul district': 'Anugul',
    'ganjam district': 'Ganjam',
    'jajapur district': 'Jajapur',
    'bargarh district': 'Bargarh',
    'dhenkanal district': 'Dhenkanal',
    'bhadrak district': 'Bhadrak',
    'nuapada district': 'Nuapada',
    'kendujhar district': 'Kendujhar',
    'mayurbhanj district': 'Mayurbhanj',
    'jharsuguda district': 'Jharsuguda',
    'kandhamal district': 'Kandhamal',
    'deogarh district': 'Deogarh',
    'sundargarh district': 'Sundargarh',
    'jagatsinghapur district': 'Jagatsinghapur',
    'balangir district': 'Balangir',
    'baleshwar district': 'Baleshwar',
    'puri district': 'Puri',
    'sonepur district': 'Sonepur',
    'khordha district': 'Khordha',
    'boudh district': 'Boudh',
    'gajapati district': 'Gajapati',
    'nayagarh district': 'Nayagarh',
    'nabarangpur district': 'Nabarangpur',
    'kendrapara district': 'Kendrapara',
    'cuttack district': 'Cuttack'
}

districts_of_punjab = {
    'shahid bhagat singh nagar district': 'Shahid Bhagat Singh Nagar',
    'fazilka district': 'Fazilka',
    'barnala district': 'Barnala',
    'mansa district': 'Mansa',
    'ludhiana district': 'Ludhiana',
    'sri muktsar sahib district': 'Sri Muktsar Sahib',
    'patiala district': 'Patiala',
    'pathankot district': 'Pathankot',
    'fatehgarh sahib district': 'Fatehgarh Sahib',
    'rupnagar district': 'Rupnagar',
    'tarn taran district': 'Tarn Taran',
    'sas nagar district': 'Sas Nagar',
    'sangrur district': 'Sangrur',
    'jalandhar district': 'Jalandhar',
    'bathinda district': 'Bathinda',
    'kapurthala district': 'Kapurthala',
    'firozepur district': 'Firozepur',
    'gurdaspur district': 'Gurdaspur',
    'amritsar district': 'Amritsar',
    'faridkot district': 'Faridkot',
    'hoshiarpur district': 'Hoshiarpur',
    'moga district': 'Moga'
}

districts_of_rajasthan = {
    'pali district': 'Pali',
    'ganganagar district': 'Ganganagar',
    'churu district': 'Churu',
    'jaipur district': 'Jaipur',
    'baran district': 'Baran',
    'bhilwara district': 'Bhilwara',
    'banswara district': 'Banswara',
    'dungarpur district': 'Dungarpur',
    'tonk district': 'Tonk',
    'jodhpur district': 'Jodhpur',
    'karauli district': 'Karauli',
    'udaipur district': 'Udaipur',
    'dausa district': 'Dausa',
    'nagaur district': 'Nagaur',
    'bharatpur district': 'Bharatpur',
    'barmer district': 'Barmer',
    'ajmer district': 'Ajmer',
    'chittorgarh district': 'Chittorgarh',
    'hanumangarh district': 'Hanumangarh',
    'pratapgarh district': 'Pratapgarh',
    'sawai madhopur district': 'Sawai Madhopur',
    'jalore district': 'Jalore',
    'bikaner district': 'Bikaner',
    'sikar district': 'Sikar',
    'dholpur district': 'Dholpur',
    'sirohi district': 'Sirohi',
    'rajsamand district': 'Rajsamand',
    'jaisalmer district': 'Jaisalmer',
    'bundi district': 'Bundi',
    'jhalawar district': 'Jhalawar',
    'alwar district': 'Alwar',
    'kota district': 'Kota',
    'jhunjhunu district': 'Jhunjhunu'
}

districts_of_sikkim = {
    'south district': 'South',
    'west district': 'West',
    'east district': 'East',
    'north district': 'North'
}

districts_of_tamilnadu = {
    "tiruchirappalli district": "Tiruchirappalli",
    "ramanathapuram district": "Ramanathapuram",
    "krishnagiri district": "Krishnagiri",
    "cuddalore district": "Cuddalore",
    "kancheepuram district": "Kancheepuram",
    "tiruppur district": "Tiruppur",
    "dharmapuri district": "Dharmapuri",
    "thoothukkudi district": "Thoothukkudi",
    "thanjavur district": "Thanjavur",
    "madurai district": "Madurai",
    "tiruvannamalai district": "Tiruvannamalai",
    "salem district": "Salem",
    "nagapattinam district": "Nagapattinam",
    "tirupathur district": "Tirupathur",
    "ariyalur district": "Ariyalur",
    "chennai district": "Chennai",
    "the nilgiris district": "The Nilgiris",
    "erode district": "Erode",
    "karur district": "Karur",
    "kallakkurichi district": "Kallakkurichi",
    "viluppuram district": "Viluppuram",
    "pudukkottai district": "Pudukkottai",
    "perambalur district": "Perambalur",
    "coimbatore district": "Coimbatore",
    "virudhunagar district": "Virudhunagar",
    "dindigul district": "Dindigul",
    "sivaganga district": "Sivaganga",
    "tenkasi district": "Tenkasi",
    "chengalpattu district": "Chengalpattu",
    "kanniyakumari district": "Kanniyakumari",
    "tirunelveli district": "Tirunelveli",
    "thiruvallur district": "Thiruvallur",
    "theni district": "Theni",
    "ranipet district": "Ranipet",
    "namakkal district": "Namakkal",
    "vellore district": "Vellore",
    "thiruvarur district": "Thiruvarur"
}

districts_of_telangana = {
    "narayanpet district": "Narayanpet",
    "nalgonda district": "Nalgonda",
    "jangaon district": "Jangaon",
    "bhadradri kothagudem district": "Bhadradri Kothagudem",
    "warangal rural district": "Warangal Rural",
    "kumuram bheem asifabad district": "Kumuram Bheem Asifabad",
    "nizamabad district": "Nizamabad",
    "adilabad district": "Adilabad",
    "rajanna sircilla district": "Rajanna Sircilla",
    "nagarkurnool district": "Nagarkurnool",
    "peddapalle district": "Peddapalle",
    "nirmal district": "Nirmal",
    "mahabubabad district": "Mahabubabad",
    "sangareddy district": "Sangareddy",
    "wanaparthy district": "Wanaparthy",
    "vikarabad district": "Vikarabad",
    "jagtial district": "Jagtial",
    "yadadri bhuvanagiri district": "Yadadri Bhuvanagiri",
    "medak district": "Medak",
    "mahbubnagar district": "Mahbubnagar",
    "jaya shankar bhalupally district": "Jaya Shankar Bhalupally",
    "warangal urban district": "Warangal Urban",
    "rangareddy district": "Rangareddy",
    "hyderabad district": "Hyderabad",
    "suryapet district": "Suryapet",
    "jogulamba gadwal district": "Jogulamba Gadwal",
    "kamareddy district": "Kamareddy",
    "mulugu district": "Mulugu",
    "medchal malkajgiri district": "Medchal Malkajgiri",
    "karimnagar district": "Karimnagar",
    "mancherial district": "Mancherial",
    "siddipet district": "Siddipet",
    "khammam district": "Khammam"
}

districts_of_tripura = {
    "unakoti district": "Unakoti",
    "khowai district": "Khowai",
    "sepahijala district": "Sepahijala",
    "north tripura district": "North Tripura",
    "dhalai district": "Dhalai",
    "south tripura district": "South Tripura",
    "gomati district": "Gomati",
    "west tripura district": "West Tripura"
}

districts_of_uttarakhand = {
    "Bageshwar District": "Bageshwar",
    "Udham Singh Nagar District": "Udham Singh Nagar",
    "Haridwar District": "Haridwar",
    "Champawat District": "Champawat",
    "Nainital District": "Nainital",
    "Dehradun District": "Dehradun",
    "Chamoli District": "Chamoli",
    "Almora District": "Almora",
    "Uttarkashi District": "Uttarkashi",
    "Pithoragarh District": "Pithoragarh",
    "Rudraprayag District": "Rudraprayag",
    "Pauri Garhwal District": "Pauri Garhwal",
    "Tehri Garhwal District": "Tehri Garhwal"
}

districts_of_uttar_pradesh = {
    "Amethi District": "Amethi",
    "Siddharthnagar District": "Siddharthnagar",
    "Auraiya District": "Auraiya",
    "Sambhal District": "Sambhal",
    "Kanpur Nagar District": "Kanpur Nagar",
    "Aligarh District": "Aligarh",
    "Mahoba District": "Mahoba",
    "Lucknow District": "Lucknow",
    "Sant Kabeer Nagar District": "Sant Kabeer Nagar",
    "Hathras District": "Hathras",
    "Budaun District": "Budaun",
    "Moradabad District": "Moradabad",
    "Kushinagar District": "Kushinagar",
    "Baghpat District": "Baghpat",
    "Shahjahanpur District": "Shahjahanpur",
    "Muzaffarnagar District": "Muzaffarnagar",
    "Ambedkar Nagar District": "Ambedkar Nagar",
    "Bahraich District": "Bahraich",
    "Jalaun District": "Jalaun",
    "Rampur District": "Rampur",
    "Ballia District": "Ballia",
    "Shravasti District": "Shravasti",
    "Kasganj District": "Kasganj",
    "Varanasi District": "Varanasi",
    "Gautam Buddha Nagar District": "Gautam Buddha Nagar",
    "Basti District": "Basti",
    "Shamli District": "Shamli",
    "Maharajganj District": "Maharajganj",
    "Etawah District": "Etawah",
    "Etah District": "Etah",
    "Banda District": "Banda",
    "Bijnor District": "Bijnor",
    "Hardoi District": "Hardoi",
    "Balrampur District": "Balrampur",
    "Amroha District": "Amroha",
    "Pilibhit District": "Pilibhit",
    "Mainpuri District": "Mainpuri",
    "Kanpur Dehat District": "Kanpur Dehat",
    "Jaunpur District": "Jaunpur",
    "Kaushambi District": "Kaushambi",
    "Hapur District": "Hapur",
    "Hamirpur District": "Hamirpur",
    "Meerut District": "Meerut",
    "Mathura District": "Mathura",
    "Chitrakoot District": "Chitrakoot",
    "Lalitpur District": "Lalitpur",
    "Mau District": "Mau",
    "Mirzapur District": "Mirzapur",
    "Bulandshahr District": "Bulandshahr",
    "Gonda District": "Gonda",
    "Jhansi District": "Jhansi",
    "Chandauli District": "Chandauli",
    "Bhadohi District": "Bhadohi",
    "Pratapgarh District": "Pratapgarh",
    "Saharanpur District": "Saharanpur",
    "Bara Banki District": "Bara Banki",
    "Bareilly District": "Bareilly",
    "Sitapur District": "Sitapur",
    "Sultanpur District": "Sultanpur",
    "Agra District": "Agra",
    "Fatehpur District": "Fatehpur",
    "Rae Bareli District": "Rae Bareli",
    "Firozabad District": "Firozabad",
    "Kheri District": "Kheri",
    "Gorakhpur District": "Gorakhpur",
    "Unnao District": "Unnao",
    "Prayagraj District": "Prayagraj",
    "Sonbhadra District": "Sonbhadra",
    "Ghazipur District": "Ghazipur",
    "Farrukhabad District": "Farrukhabad",
    "Kannauj District": "Kannauj",
    "Azamgarh District": "Azamgarh",
    "Ayodhya District": "Ayodhya",
    "Deoria District": "Deoria",
    "Ghaziabad District": "Ghaziabad"
}

districts_of_west_bengal = {
    "South Twenty Four Parganas District": "South Twenty Four Parganas",
    "Purba Bardhaman District": "Purba Bardhaman",
    "Uttar Dinajpur District": "Uttar Dinajpur",
    "Kalimpong District": "Kalimpong",
    "Murshidabad District": "Murshidabad",
    "Paschim Medinipur District": "Paschim Medinipur",
    "Dakshin Dinajpur District": "Dakshin Dinajpur",
    "Jalpaiguri District": "Jalpaiguri",
    "Purulia District": "Purulia",
    "North Twenty Four Parganas District": "North Twenty Four Parganas",
    "Bankura District": "Bankura",
    "Jhargram District": "Jhargram",
    "Howrah District": "Howrah",
    "Hooghly District": "Hooghly",
    "Kolkata District": "Kolkata",
    "Koch Bihar District": "Koch Bihar",
    "Alipurduar District": "Alipurduar",
    "Paschim Bardhaman District": "Paschim Bardhaman",
    "Nadia District": "Nadia",
    "Birbhum District": "Birbhum",
    "Purba Medinipur District": "Purba Medinipur",
    "Maldah District": "Maldah",
    "Darjiling District": "Darjiling"
}

districts_of_andaman_nicobar = {
    "North and Middle Andaman District": "North and Middle Andaman",
    "South Andaman District": "South Andaman",
    "Nicobars District": "Nicobars"
}

districts_of_daman_diu = {
    "Diu District": "Diu",
    "Daman District": "Daman",
    "Dadra and Nagar Haveli District": "Dadra and Nagar Haveli"
}

districts_of_lakshadweep = {
    "Lakshadweep District": "Lakshadweep"
}

districts_of_delhi = {
    "South District": "South",
    "Central District": "Central Delhi",
    "New Delhi District": "New Delhi",
    "West District": "West",
    "South West District": "South West",
    "South East Delhi District": "South East Delhi",
    "Shahdara District": "Shahdara",
    "North East District": "North East",
    "East District": "East",
    "North West District": "North West",
    "North District": "North"
}

districts_of_puducherry = {
    "Karaikal District": "Karaikal",
    "Puducherry District": "Puducherry",
    "Yanam District": "Yanam",
    "Mahe District": "Mahe"
}

districts_of_ladakh = {
    "Kargil District": "Kargil",
    "Leh Ladakh District": "Leh Ladakh"
}


def insert_static_district_values_table(cursor):
    insert_district_values(cursor, 'andhra-pradesh', districts_of_andhra_pradesh)
    insert_district_values(cursor, 'arunachal-pradesh', districts_of_arunachal_pradesh)
    insert_district_values(cursor, 'assam', districts_of_assam)
    insert_district_values(cursor, 'bihar', districts_of_bihar)
    insert_district_values(cursor, 'chandigarh', districts_of_chandigarh)
    insert_district_values(cursor, 'chhattisgarh', districts_of_chhattisgarh)
    insert_district_values(cursor, 'goa', districts_of_goa)
    insert_district_values(cursor, 'gujarat', districts_of_gujarat)
    insert_district_values(cursor, 'haryana', districts_of_haryana)
    insert_district_values(cursor, 'himachal-pradesh', districts_of_himachal_pradesh)
    insert_district_values(cursor, 'jammu-&-kashmir', districts_of_jammu_kashmir)
    insert_district_values(cursor, 'jharkhand', districts_of_jharkhand)
    insert_district_values(cursor, 'karnataka', districts_of_karnataka)
    insert_district_values(cursor, 'kerala', districts_of_kerala)
    insert_district_values(cursor, 'madhya-pradesh', districts_of_madhya_pradesh)
    insert_district_values(cursor, 'maharashtra', districts_of_maharashtra)
    insert_district_values(cursor, 'manipur', districts_of_manipur)
    insert_district_values(cursor, 'meghalaya', districts_of_meghalaya)
    insert_district_values(cursor, 'mizoram', districts_of_mizoram)
    insert_district_values(cursor, 'nagaland', districts_of_nagaland)
    insert_district_values(cursor, 'odisha', districts_of_odisha)
    insert_district_values(cursor, 'punjab', districts_of_punjab)
    insert_district_values(cursor, 'rajasthan', districts_of_rajasthan)
    insert_district_values(cursor, 'sikkim', districts_of_sikkim)
    insert_district_values(cursor, 'tamil-nadu', districts_of_tamilnadu)
    insert_district_values(cursor, 'telangana', districts_of_telangana)
    insert_district_values(cursor, 'tripura', districts_of_tripura)
    insert_district_values(cursor, 'uttarakhand', districts_of_uttarakhand)
    insert_district_values(cursor, 'uttar-pradesh', districts_of_uttar_pradesh)
    insert_district_values(cursor, 'west-bengal', districts_of_west_bengal)
    insert_district_values(cursor, 'andaman-&-nicobar-islands', districts_of_andaman_nicobar)
    insert_district_values(cursor, 'dadra-&-nagar-haveli-&-daman-&-diu', districts_of_daman_diu)
    insert_district_values(cursor, 'lakshadweep', districts_of_lakshadweep)
    insert_district_values(cursor, 'delhi', districts_of_delhi)
    insert_district_values(cursor, 'puducherry', districts_of_puducherry)
    insert_district_values(cursor, 'ladakh', districts_of_ladakh)


def get_district_id_by_key(cursor, district_name):
    query = "SELECT id FROM Districts WHERE district_key = %s;"
    cursor.execute(query, (district_name,))
    result = cursor.fetchone()
    return result[0] if result else None


def get_district_id_by_value(cursor, district_name):
    query = "SELECT id FROM Districts WHERE district_value = %s;"
    cursor.execute(query, (district_name,))
    result = cursor.fetchone()
    return result[0] if result else None
