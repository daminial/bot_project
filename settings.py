"""The module contains the settings of the demo."""

# import contextlib
import os
from dotenv import load_dotenv

# with contextlib.suppress(ImportError):
#     from dotenv import load_dotenv
#     load_dotenv()

load_dotenv()    
TOKEN = os.getenv('TOKEN_BOT')
