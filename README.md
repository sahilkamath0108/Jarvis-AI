J.A.R.V.I.S (Personal AI Assistant)
J.A.R.V.I.S is a versatile AI assistant designed to streamline interactions through natural language understanding and automation. Here's an overview of the technologies and features integrated into J.A.R.V.I.S:

Technologies Utilized:
Image Generation: Implemented Text-to-Image generation using HuggingFace stabilityai/stable-diffusion-xl-base-1.0 model

Speech Recognition: Speech recognition using the SpeechRecognition library, allowing for seamless voice-based interactions.

Natural Language Processing (NLP): Integrated NLP capabilities to understand and respond to natural language queries effectively.

OpenAI's GPT-3.5 Turbo: Leveraged OpenAI's powerful language model for advanced language understanding and generation.

Hugging Face Transformers: Employed various Hugging Face models, including falcon-7b/40b, google/flan-t5-xl, Roberta, and more, to enhance language processing and understanding.

Langchain and LangSmith: Explored Langchain and LangSmith for enhanced language capabilities and interaction.

ChromaDB: Utilized ChromaDB for managing vector databases, enabling efficient information retrieval.

Key Features:
PDF Question-Answering (QA): Integrated a RetrievalQA Chain along with Vector DB to provide accurate responses to questions from PDF documents.

Text-to-Speech: Enabled text-to-speech capabilities, allowing J.A.R.V.I.S to speak responses.

AI Chat: Implemented a chatbot feature, enabling dynamic and interactive conversations with the AI assistant.

Web Interactions: Leveraged web scraping and automation using Python scripts, including web interactions with Selenium, for seamless task handling.

Real-Time Data: Integrated APIs and web scraping to fetch real-time data, keeping responses up-to-date.

Google Search: Incorporated Google search capabilities for quick access to information from the web.

Experience Gained:
During the development of J.A.R.V.I.S, I gained hands-on experience with a variety of cutting-edge technologies, including:

OpenAI models (GPT 3.5, DaVinci)
Hugging Face models (falcon-7b/40b, google/flan-t5-xl, Roberta, etc)
Working with vector databases such as ChromaDB
Developing and fine-tuning Transformer models

# How to use
Clone the repo and create .env file with your keys for
OPENAI_API_KEY
HG_FACE
Run main.py , go through the if else conditions to know about what can be done with JARVIS

Few Images generated using diffusion models

![Metaverse](images/metaverse.jpg)
*Meteaverse*

![Futuristic World](images/futuristic.jpg)
*Futuristic World*
