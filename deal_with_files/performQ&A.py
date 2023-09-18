from helpers.say import say
from helpers.listen import listen
from langchain.vectorstores import Chroma
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 
from transformers import pipeline
import torch
from langchain.llms import HuggingFacePipeline
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA

chat_history = []

def ques_ans():
    say('Alright shoot questions at me')
    while True:
        query = listen()
        if query:
            for conversation in chat(chat_history, query):
                chat_history.append(conversation)
        latest_conversation = chat_history[-1]
        user_input, bot_response = latest_conversation
        say(bot_response)
            

def chat(chat_history, user_input):

    bot_response = qa_chain({"query": user_input})
    bot_response = bot_response['result']
    response = ""
    for letter in ''.join(bot_response):
        response += letter + ""
        yield chat_history + [(user_input, response)]

checkpoint = "MBZUAI/LaMini-Flan-T5-783M"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint,
    device_map="auto",
    torch_dtype = torch.float32)

embeddings = SentenceTransformerEmbeddings(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1")

db = Chroma(persist_directory="data", embedding_function=embeddings)

pipe = pipeline(
    'text2text-generation',
    model = base_model,
    tokenizer = tokenizer,
    max_length = 512,
    do_sample = True,
    temperature = 0.3,
    top_p= 0.95
)
local_llm = HuggingFacePipeline(pipeline=pipe)

qa_chain = RetrievalQA.from_chain_type(llm=local_llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_type="similarity", search_kwargs={"k":2}),
        return_source_documents=True,
        )


if __name__ == "__main__":
    print('how much stipend')

