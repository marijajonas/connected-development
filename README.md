Connected Development

Exploring the relationships between digital access, education, and economic development.

1. Project Overview

Connected Development is a data engineering and exploratory research project investigating relationships between technological access, education, and economic development across countries over time.

The project aims to build a reproducible data pipeline that collects, processes, validates, and stores international development indicators in a relational database.

2. Research Question

How do internet access, educational attainment, and economic prosperity relate across countries, and how have these relationships changed over time?

Research objectives

- Explore the relationship between internet adoption and GDP per capita.
- Investigate how secondary school enrollment relates to digital access and economic development.
- Compare development patterns across countries and regions.
- Identify trends, missing data, and unusual observations.

The analysis will focus on associations rather than assuming causal relationships.

3. Data Sources

Primary source: "World Bank Open Data" (https://data.worldbank.org/)

Dataset: World Development Indicators (WDI).

Selected indicators:

Indicator| Code
Individuals using the Internet (% of population)| IT.NET.USER.ZS
GDP per capita, PPP (constant 2021 international $)| NY.GDP.PCAP.PP.KD
School enrollment, secondary (% gross)| SE.SEC.ENRR

Initial target period: 2000–2022.

4. Technologies

- Python – data extraction and transformation
- Pandas – data processing and cleaning
- Requests – API communication
- SQLite – relational database
- SQL – querying and analysis
- Git and GitHub – version control and project documentation

5. Project Architecture

The planned workflow:

1. Extract data from the World Bank API.
2. Preserve original source files.
3. Transform and validate observations using Python.
4. Store structured data in a relational database.
5. Query and analyze the data using SQL.
6. Present findings through visualizations and documentation.

6. Repository Structure

connected-development/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── database-schema.png
└── .gitignore

7. Project Status

Currently in Week 1: research question definition, data-source exploration, and preliminary database design.

The data ingestion and transformation pipeline will be developed in the following stages.

8. Limitations

- Data availability may vary between countries and years.
- Different indicators may have different reporting methodologies.
- Correlation does not establish causation.
- Results will depend on data coverage and the selected time period.

9. Future Development

Potential extensions include forecasting, additional development indicators, automated data ingestion, and migration to PostgreSQL.
