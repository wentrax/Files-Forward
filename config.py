import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "16448144"))
    API_HASH = os.environ.get("API_HASH", "1073665850700150caf0e0cbb68216a2")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5910326190:AAGJ4GkXP4uEwCMGSvaMBZpqB7nYqOIYHoE")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = "1533128706"                            
    DATABASE_URI = "mongodb+srv://filesautobot:filesautobot870@cluster0.qcxdkpw.mongodb.net/?retryWrites=true&w=majority" 
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = "AgAzyuPpG3pe4-tVXeTUUdXnWr8oZ0-IoEtWCVuh-cKdmQ9UGq8WpRsqPLvPAQsmcTmMyuhdfAsUm_Ht-MZCmoR5EwwlXKIp8itDLUuIl9eD5l8ylNTZYG4A8o3zr-Q1b9URiwEHAZp5C0Pb0brukrpPQffxk6p-j0BYDZWLqsUARJyOci1NCzyJdj3VhPxWNV-ia7nT4QN-KYxyMw0uiypZoj3FT2ASWE-htgd70zn3jj0Glfzv4u7k_9Yhi8rIPqaUqlbnqdVcX_DVwd8d5FsahzfhxCs3soejUtSgUPfTZ2tb72QPNetnfsITLly_WyIuFiJ1_ifNRF2m7NR2lPWAAAAAATPH6AEA" 
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001922400671"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "FilesForwardV2Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
