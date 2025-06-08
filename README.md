# Memvid Demo Project

This project demonstrates the use of [Memvid](https://github.com/olow304/memvid), a video-based AI memory system that enables lightning-fast semantic search across text data.

## Setup

### 1. Create and activate a virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install dependencies

```bash
# Install memvid and required packages
pip install memvid PyPDF2 python-dotenv
```

### 3. Set up environment variables

Copy the example environment file and add your API keys:

```bash
cp .env_example .env
```

Then edit the `.env` file to add your API keys. You only need to add the API key for the provider you plan to use.

## Usage

### Chat with a PDF

The main script `pdf_chat.py` allows you to chat with a PDF document. It processes the PDF, creates a video memory, and then allows you to interact with the content through a chat interface.

```bash
# Use OpenAI as the provider (default)
python pdf_chat.py --provider openai

# Or use Google
python pdf_chat.py --provider google

# Or use Anthropic
python pdf_chat.py --provider anthropic
```

### How it works

1. The script reads the PDF file specified in the code
2. It processes the text into chunks and encodes them into a video file
3. It creates an index file to enable fast retrieval
4. It starts a chat session where you can ask questions about the content
5. Type 'q', 'quit', or 'exit' to end the chat session

## Customization

You can modify the `pdf_chat.py` script to:

- Change the PDF file path
- Adjust chunk size and overlap
- Configure video encoding parameters
- Change the LLM model

## Troubleshooting

If you encounter issues:

1. Make sure your API key is correctly set in the `.env` file
2. Ensure you have installed the required packages for your chosen provider:
   - For OpenAI: `pip install openai`
   - For Google: `pip install google-generativeai`
   - For Anthropic: `pip install anthropic`
3. Check that the PDF file exists and is readable

## License

This project is licensed under the MIT License - see the original [Memvid repository](https://github.com/olow304/memvid) for details.
