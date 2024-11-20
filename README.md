# NaturalQ Project

Welcome to the NaturalQ Project! This innovative project is designed to revolutionize how you interact/converse with your data, allowing seamless conversions from natural language queries to SQL commands. As part of the eavluation and validation of existing tool/ open-source projects that can be used, NaturalQ utilizes powerful integrations, including Vanna.ai, Snowflake, and Flask, enabling intuitive and accessible data exploration.

## Overview

NaturalQ empowers users to interact with data stored across various platforms using natural language. By leveraging advanced AI models, it translates user queries into precise SQL commands, democratizing data analysis for both technical and non-technical users.

## Key Features

- **Natural Language Processing:** Converts plain language questions into SQL queries, facilitating easy data interactions.
- **Contextual Awareness:** Adapts to specific database structures and nuances for accurate query generation.
- **Versatile Integration:** Compatible with a wide range of databases, including Snowflake, ClickHouse, MySQL, and PostgreSQL.
- **Secure Interaction:** Ensures data safety through robust access controls and encryption practices.

## Components

### Vanna.ai

Vanna.ai is a cornerstone of the NaturalQ project, utilizing large language models for generating SQL from natural language. With features like retrieval-augmented generation (RAG), it enhances accuracy and user friendliness.

### Snowflake

While Snowflake serves as an example database, NaturalQ's design supports integration with various data storage solutions. Snowflake provides scalable and secure data management, optimizing query performance.

### Flask

Flask offers an adaptable framework for building custom user interfaces, ensuring a seamless and intuitive interaction experience for end-users.

## Installation

To get started with, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/your-repo/naturalQ.git
cd naturalQ
pip install -r requirements.txt
```

Configure your database settings and API keys in the provided configuration files.

## Usage

### Running the Application

Launch the interface using Flask:

```bash
from vanna.flask import VannaFlaskApp

app = VannaFlaskApp(vn)
app.run()
```

### Sample Queries

Once set up, use the app to explore your data with natural language queries. Here are some examples:

```python
vn.ask('Analyze the distribution of alerts across severity levels to prioritize incident responses.')
vn.ask('List the most common threats detected by SentinelOne and CrowdStrike.')
```

## Future Enhancements

Our vision is to expand NaturalQ by integrating more components, enabling seamless interaction with diverse data sources. Stay tuned for updates and new features aimed at enhancing the overall experience.

## Contributing

We welcome contributions to the NaturalQ project. Please fork the repository and submit pull requests for improvements or new features. For major changes, open an issue first to discuss potential modifications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
