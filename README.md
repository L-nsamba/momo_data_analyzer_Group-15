<h1 align="center"> 💰 MOBILE MONEY ANALYZER </h1>

### 📋 PROJECT OVERVIEW

This project is an enterprise-level full-stack application designed to process, clean and visualize Mobile Money (M0MO) transaction data. 
The system extracts data from XML SMS, categorizes transactions (e.g sent, received, payments) using a Python-based ETL (Extract, Transform, Load) pipeline, stores them in a relational MYSQL database and presents insights via a web-based front-end display.
<br>

### 👥 GROUP 15 TEAM MEMBERS
1. Leon Nsamba
2. Mitchell Barure
3. Mufaro Kunze
4. Uwera Ruth Queen
5. Michael Okinyi Odhiambo

### 🛠 PROJECT PLAN & ARCHITECTURE

**Link to System Architecture**: https://drive.google.com/file/d/11VwjXPzEtyVcKTR5qhzlJlR3nYDVkgLP/view?usp=sharing
<br>

**Link to Database Design Documentation**: https://docs.google.com/document/d/1L_9i8k3eY0Be9_FVFDM8Ej2VtT09MRbBnJ2p_HC2gcQ/edit?usp=sharing
<br>

**Link to EWD AI Log Documentation**: https://docs.google.com/document/d/1pGzeU6sfVQJjUu1Yf0Ksqrh-R3pc5Tpnkw56t4HX5KU/edit?usp=sharing
<br>

### 🚀 GETTING STARTED FOR THE PROJECT

1. Clone the repo: ``` git clone https://github.com/L-nsamba/momo_data_analyzer_Group-15.git ```
2. Install dependencies: ```pip install -r requirements.txt```
3. Run ETL: Execute ```./scripts/run_etl.sh``` to process the momo.xml data.

### 📂 PROJECT STRUCTURE

The project structure is as follows;
```plaintext
├──.idea/                
├── analytics/           # Contains logic for analyzing processed data
├── api/                 # Handles communication between the backend and frontend
├── data/                # Contains XML --> JSON
├── database/            # Database schemas, migrations and connection logic
├── docs/                # Project documentation (ERD diagrams, notes)
├── dsa/                 # Linear & Binary Search Logic
├── etl/                 # Contains the ETL pipeline
├── examples/            # Sample JSON
├── scripts/             # Utility and helper scripts
├── tests/               # Contains automated tests
├── web/
│   ├── chart_handler.js   # Fetches data from API
│   └── styles.css         # Controls the visual appearance
│
├── .env.example        # Shows required environment variables
├── README.md           # Description of the project
├── index.html          # Main entry point for the UI
└── requirements.txt    # List of the Python dependencies
```

### ⚙ SYSTEM WORKFLOW

1. Data Extraction
   * XML SMS files containing Momo transactions are read and parsed
     
2. Data Transformation
   * Messages are cleaned, categorized and normalized
   * Transaction types such as sent, received, payments, and withdrawals are identified.
     
3. Data Loading
   * Cleaned data is stored in MYSQL database following the ERD design
     
4. API layer
   * Processed data is exposed via RESTful endpoints.
   
6. Visualization
   * The web interface fetches data from the API and displays insights using charts.

### 🗃️ DATABASE DESIGN
**Link to Entity Relationship Diagram (ERD)**: https://drive.google.com/file/d/1E8zs6vlPjvkJVyE-KlzCFYkeHmhW4Ba_/view?usp=sharing

| Table Name | Purpose |
|----------- | --------|
| Users      |  Stores user profiles (customers, agents) |
| transaction_categories | Shows item categories and sub-categories for transactions |
| transactions | Records all financial transactions between users |
| user_category | Maps users to categories (M:M relationship)
| system_logs | Contains processing status of transactions | 

### 🔗 Key Relationships
<li> transactions.sender_id and transactions.receiver_id references user.user_id </li>
<li> transactions.category_id --> transaction_categories.category_id </li>
<li> user_category --> bridges users and transaction_categories </li>

### 📝 Design Highlights
<li> Use of foreign keys to enforce referential integrity. </li>
<li> ENUMS for status tracking in system_logs. </li>
<li> Composite primary key in user_category to prevent duplicate mappings. </li>
<li> Timestamp fields (created_at, processed_at)</li>
<li> Normalization to avoid data duplication </li>
<li>JSON Data Modelling</li>

### 📜📑 SCRUM BOARD SETUP
 

**Link to Scrum Board**: https://trello.com/b/5OkdDdek/momo-sms-analyser-scrum-board





















