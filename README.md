<h1 align="center"> 💰 MOBILE MONEY ANALYZER </h1>

### 📋 PROJECT OVERVIEW

This project is an enterprise-level full-stack application designed to process, clean and visualize Mobile Money (M0MO) transaction data. 
The system extracts data from XML SMS, categorizes transactions (e.g sent, recieved, payments) using a Pyhton-based ETL (Extract, Transform, Load) pipeline, stores them in a relational MYSQL database and presents insights via a web-based front-end display.
<br>

### 👥 GROUP 15 TEAM MEMBERS
1. Leon Nsamba
2. Mitchell Barure
3. Mufaro Kunze
4. Uwera Ruth Queen
5. Michael Okinyi Odhiambo

### 🛠 PROJECT PLAN & ARCHITECTURE

**Link to System Architecture**: https://drive.google.com/file/d/11VwjXPzEtyVcKTR5qhzlJlR3nYDVkgLP/view?usp=sharing


### 📂 PROJECT STRUCTURE

The project structure is as follows;
```plaintext
├── analytics/          # Contains logic for analyzing processed data
├── api/                # Handles communication between the backend and frontend
├── data/               # stores all application data 
├── etl/                # Contains the ETL pipeline 
├── scripts/            # Utility and helper scripts
├── tests/              # Contains automated tests
├── web/
│   ├── chart_handler.js   # Fetches data from API
│   └── styles.css         # Controls the visual appearence
│
├── .env.example        # Shows required environment variables
├── README.md           # Description of the project
├── index.html          # Main entry point for the UI
└── requirements.txt    # Lists of the python dependencies
```


### 🚀 GETTING STARTED FOR THE PROJECT

1. Clone the repo: ``` git clone https://github.com/L-nsamba/momo_data_analyzer_Group-15.git ```
2. Install dependencies: ```pip install -r requirements.txt```
3. Run ETL: Execute ```./scripts/run_etl.sh``` to process the momo.xml data.

### 📜📑 SCRUM BOARD SETUP

 Our team follows a simple but effective format containing:
 
 * To Do: Repo setup, architecture diagram, research
 * In Progress: ETL logic development
 * Done: Initial project organization

**Link to Scrum Board**: 














