# Assignment_04
Link to the application:

[Codelab]()

[Demo]()

# Problem Statement:

**Problem Statement:**

This data engineering project requires a comprehensive approach to effectively leverage Snowflake marketplace datasets for a meaningful use case. The primary challenge is to integrate diverse datasets cohesively. The team collaboratively developed a thematic story around these datasets, defining use cases that addresses a specific problem. This involves programming SQL processes and User Defined Functions to achieve use cases. Git actions has been used for deployment purposes introducing continuous integration and deployment (CI/CD).

The integration of Snowflake with Streamlit adds another layer for the user. The objective is to enable the creation of analytics based on processed data and develop a text-based SQL query feature capable of interpreting user natural language input. This involves retrieving table schema using the Langchain OpenAI service, integrating it into the query prompt for user-friendly interaction. The Streamlit application presents the generated raw SQL code to users, allowing for updates or feedback to the OpenAI API.

Testing the system is imperative, involving the creation of at various test cases. These tests covers scenarios where SQL code generation works seamlessly, where it fails initially but can be corrected with query prompt modifications, and where failures persist despite multiple attempts. The final deployment phase involves deploying the application to a public cloud platform, Streamlit Cloud, ensuring public access. This introduces challenges related to scalability, security, and reliability that need careful consideration to guarantee a successful and user-friendly deployment.

# Technologies Used:

1. GitHub
2. Python
3. LangChain
4. OpenAI
5. Snowflake
6. Streamlit

# Data Source:
1. ![OAG_FLIGHT_EMISSIONS_DATA_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ3D?originTab=databases&database=OAG_FLIGHT_EMISSIONS_DATA_SAMPLE)
2. ![OAG_FLIGHT_STATUS_DATA_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ42?originTab=databases&database=OAG_FLIGHT_STATUS_DATA_SAMPLE)
3. ![OAG_GLOBAL_AIRLINE_SCHEDULES_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ39?originTab=databases&database=OAG_GLOBAL_AIRLINE_SCHEDULES_SAMPLE)

# Project Structure:



# Team Contribution:

| Name            | Contribution % | Contributions |
|-----------------|----------------|---------------|
| Naman Gupta     |     33.3%      |  Dataset Exploration, Use Case building, SQL Processes & UDF Creation, CI-CD pipeline     |
| Jagruti Agrawal |     33.3%      |  Dataset Exploration, Use Case building, SQL Processes & UDF Creation, Architecture development            |
| Divyesh Rajput  |     33.3%      |  Dataset Exploration, Use Case building, Chat-bot development with Langchain & OpenAI          |
