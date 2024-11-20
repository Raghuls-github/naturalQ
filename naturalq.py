# -*- coding: utf-8 -*-
"""naturalQ.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14QuwBnpcb6N1TZ3izr8rrWMb-9c50DMZ

# **NaturalQ** - "Conversion of natural language to SQL queries using LLMs"
🧠 **NaturalQ** is a project is aimed to enable users to make conversations with the data that they want to know more about. This tool comprises of multiple components out of which vanna.ai is one of the integration that could streamline the process of converting natural language to SQL queries in a robust manner.

### ⚙️ Installing the required dependencies

*   vanna[chromadb,openai,snowflake]


##### 🛠 For making any chnages to the source code of the vanna.ai, kindly fork the repository using https://github.com/vanna-ai/vanna
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install 'vanna[chromadb,openai,snowflake]'

"""### 📲 Import the libraries
- The imports can be changed as per the LLMs, VectorDB and Databases with which we want to build the tool. (**Bring Your Own [LLM, VectorDB, DB]**)
"""

from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore

"""### Initializing the class MyVanna"""

class MyVanna ( ChromaDB_VectorStore , OpenAI_Chat ) :
    def __init__ ( self , config=None ) :
        ChromaDB_VectorStore.__init__ ( self , config = config )
        OpenAI_Chat.__init__ ( self , config = config )


# Connecting to openAI gpt-4o
vn = MyVanna ( config = {
    'api_key' : 'your-openai-api-key' ,
    'model' : 'gpt-4o'} )

"""### 🔌 Connecting to the Snowflake Database using the vanna.ai native library connect_to_snowflake"""

vn.connect_to_snowflake ( account = "your-account" , username = "username" , password = "password" ,
                          database = "your-database" , role = "your-role" , )

"""### 💾 Training the model specific to the DB"""

df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

plan = vn.get_training_plan_generic(df_information_schema)
vn.train(plan=plan)

# DDL statements are powerful because they specify table names, colume names, types, and potentially relationships
vn.train(ddl="""
    CREATE TABLE IF NOT EXISTS my-table (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")


# Add SQL queries to your training data. This is useful if you have some queries already laying around.
vn.train ( sql = """
         SELECT
       timeGenerated::DATE AS alert_date,
       COUNT(*) AS total_alerts
   FROM
       AzureSentinel
   GROUP BY
       alert_date
   ORDER BY
       alert_date;
         """ )

# At any time you can inspect what training data the package is able to reference
training_data = vn.get_training_data()
training_data

# You can remove training data if there's obsolete/incorrect information.
vn.remove_training_data(id='1-ddl')

"""## Asking the AI"""

# Sample Questions that can be ased to the trained model
vn.ask(question= 'Analyze the distribution of alerts across severity levels to prioritize incident responses.')

vn.ask(question= 'List the most common threats or process names detected by SentinelOne and CrowdStrike.')

vn.ask(question = 'Give me the total number of alerts from sentinelone, splunk and azure sentinel')

vn.ask(question = 'Analyze the distribution of alerts across severity levels to prioritize incident responses')

vn.ask(question = 'Compare the number of alerts generated each day by SentinelOne and AzureSentinel')

vn.ask(question = 'Calculate MTTR for network issues using SolarWinds logs')

"""### 💻 Flask Application (Vanna.ai Native Flask Application)
- You can build your own flask application or use streamlit custo templates to create a chat interface.
- With this you can also consume the native UI features of the Vanna.ai as show below.
"""

from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run()
