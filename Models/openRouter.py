import os
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenRouter(model="nvidia/nemotron-3-super-120b-a12b:free")