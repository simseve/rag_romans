# Telegram Bot Using RAG with Llama-Index and MISTRAL 7B

## Overview
This Telegram bot is built using the Retrieval-Augmented Generation (RAG) framework, incorporating the llama-index library and the MISTRAL 7B model. It is designed to ingest documents and provide responses based on these documents when interacting with users on Telegram.

## Acknowledgments
In building this project, I drew inspiration from the following authors:

- [Iago Modesto Brandão](https://medium.com/poatek/building-open-source-llm-based-chatbots-using-llama-index-e6de9999ee76): Article on building open-source LLM-based chatbots using llama-index.
- [Massimo Chiriatti](https://llamabox.eu/2023/12/28/Esperimenti-di-RAG-Diario.html?fbclid=IwAR24fFeprjiO5XbwI0Z1CTdZSChbnmEX00d3AaSzTsnPt23z8JnBgHvwbQo): Article on experiments with RAG (Retrieval-Augmented Generation).


## Features
- **Document Ingestion**: Automates the ingestion of documents from a specified directory.
- **Interactive Chat**: Users can ask questions and receive answers based on the ingested documents.
- **RAG Infrastructure**: Utilizes RAG for enhanced natural language processing.
- **MISTRAL 7B Model**: Leverages the MISTRAL 7B model for advanced language understanding and generation.

## Prerequisites
- Python 3.10
- Telegram Bot API Token.
- MISTRAL7B running locally 

## Setup
1. **Clone the Repository**:
   ```bash
   git clone [Repository-URL]
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run MISTRAL**:
   - Run `ollama run mistral`. On MacOS install OLLAMA (Works on Apple silicon, tested on M2)
   - Better to use a machine with NVIDIA GPU and install OLLAMA with a docker 

5. **Configure Environment Variables**:
   - Create a `.env` file in your project root by renaming `.env.example`.
   - Add the following line with your Telegram Bot Token:
     ```
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     ```
6. **Prepare Documents Directory**:
   - Place the documents for ingestion in the `./docs` directory.

## Running the Bot
To run the bot, execute the following command:
```bash
python app.py
```

## Usage
- **Start the Bot**: Send the `/start` command in Telegram to initialize the bot.
- **Ask Questions**: Type your queries in the chat to get responses.
- **Help**: Use the `/help` command for additional information.

## Logging
- The bot includes logging to track operations and diagnose issues.
- Logs provide insights into the bot's performance and error handling.

## Contributing
Contributions to the project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the GPL3 - see the LICENSE file for details.

## Contact
For support or queries, reach out to Simone Severini.