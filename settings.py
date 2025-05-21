"""The module contains the settings of the demo."""

import contextlib
import os

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv
    load_dotenv()
    
TOKEN = os.getenv('TOKEN', '8156875158:AAHbsYUGP511G7A-S38vVPnds5amiOlkCwc')
