from memvid import MemvidEncoder, MemvidChat
import os
import sys
import argparse
from dotenv import load_dotenv

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Chat with a PDF using Memvid')
parser.add_argument('--provider', type=str, default='openai', choices=['openai', 'google', 'anthropic'],
                    help='LLM provider to use (default: openai)')
args = parser.parse_args()

# Load environment variables from .env file
load_dotenv()

# Set API key based on provider
if args.provider == 'openai':
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        print(f"OpenAI API key set in environment variables")
    else:
        print("Warning: No OpenAI API key found in .env file")
elif args.provider == 'google':
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        os.environ['GOOGLE_API_KEY'] = api_key
        print(f"Google API key set in environment variables")
    else:
        print("Warning: No Google API key found in .env file")
elif args.provider == 'anthropic':
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        os.environ['ANTHROPIC_API_KEY'] = api_key
        print(f"Anthropic API key set in environment variables")
    else:
        print("Warning: No Anthropic API key found in .env file")

print(f"Using {args.provider} as the LLM provider")

# Your PDF file
book_pdf = "the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf"  # Replace with your PDF path

# Build video memory
encoder = MemvidEncoder()
encoder.add_pdf(book_pdf)
encoder.build_video("book_memory.mp4", "book_index.json")

# Chat with the book using MemvidChat
try:
    chat = MemvidChat("book_memory.mp4", "book_index.json", llm_provider=args.provider)
    chat.start_session()

    # Start interactive chat session
    print("\nChat session started. Type 'q' to quit.")
    print("--------------------------------------------------")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            break
        response = chat.chat(user_input)
        print(f"\nMemvid: {response}")
except Exception as e:
    print(f"\nError: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure you have the required API key set in your .env file")
    print("2. Check if the provider you selected is installed (openai, google-generativeai, or anthropic)")
    print("3. Verify that the video and index files were created successfully")
    sys.exit(1)