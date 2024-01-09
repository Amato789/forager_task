"""
This script is used to get API KEY from .env.

Author: Maksym Sydorchuk
Data: 8/01/2024
"""

import os

from dotenv import load_dotenv

load_dotenv()

HUNTER_API_KEY = os.environ.get('HUNTER_API_KEY')
