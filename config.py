import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = "1533128706"                            
    DATABASE_URI = "mongodb+srv://filesautobot:filesautobot870@cluster0.qcxdkpw.mongodb.net/?retryWrites=true&w=majority" 
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = "AgAzyuPpG3pe4-tVXeTUUdXnWr8oZ0-IoEtWCVuh-cKdmQ9UGq8WpRsqPLvPAQsmcTmMyuhdfAsUm_Ht-MZCmoR5EwwlXKIp8itDLUuIl9eD5l8ylNTZYG4A8o3zr-Q1b9URiwEHAZp5C0Pb0brukrpPQffxk6p-j0BYDZWLqsUARJyOci1NCzyJdj3VhPxWNV-ia7nT4QN-KYxyMw0uiypZoj3FT2ASWE-htgd70zn3jj0Glfzv4u7k_9Yhi8rIPqaUqlbnqdVcX_DVwd8d5FsahzfhxCs3soejUtSgUPfTZ2tb72QPNetnfsITLly_WyIuFiJ1_ifNRF2m7NR2lPWAAAAAATPH6AEA" 
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
