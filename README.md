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

### 🛠 PROJECT PLAN, ERD & ARCHITECTURE

**Link to System Architecture**: https://drive.google.com/file/d/11VwjXPzEtyVcKTR5qhzlJlR3nYDVkgLP/view?usp=sharing
<br>
**Link to Entity Relationship Diagram (ERD)**: https://drive.google.com/file/d/1E8zs6vlPjvkJVyE-KlzCFYkeHmhW4Ba_/view?usp=sharing
<br>
**Link to Design Decision Documentation**: https://docs.google.com/document/d/1L_9i8k3eY0Be9_FVFDM8Ej2VtT09MRbBnJ2p_HC2gcQ/edit?usp=sharing


### 📂 PROJECT STRUCTURE

The project structure is as follows;
```plaintext
├──.idea/              # IDE configuration files
├── analytics/          # Contains logic for analyzing processed data
├── api/                # Handles communication between the backend and frontend
├── database/            # Database schemas, migrations and connection logic
├── docs/               # Project documentation (ERD diagrams, notes)
├── dsa/                # Data structures & algorithms used for parsing and processing
├── etl/                # Contains the ETL pipeline
├── examples/           # Sample inputs and example outputs
├── scripts/            # Utility and helper scripts
├── tests/              # Contains automated tests
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
     
### 🚀 GETTING STARTED FOR THE PROJECT

1. Clone the repo: ``` git clone https://github.com/L-nsamba/momo_data_analyzer_Group-15.git ```
2. Install dependencies: ```pip install -r requirements.txt```
3. Run ETL: Execute ```./scripts/run_etl.sh``` to process the momo.xml data.

### 📜📑 SCRUM BOARD SETUP

 Our team follows a simple but effective format containing:
 
 * To Do: Repo setup, architecture diagram, research
 * In Progress: ETL logic development
 * Done: Initial project organization

**Link to Scrum Board**: https://trello.com/b/5OkdDdek/momo-sms-analyser-scrum-board


















