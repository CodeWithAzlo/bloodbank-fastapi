# config.py

import os
import json
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# Load ADMIN_USERS from JSON string to dictionary, and only admins can login and see the dashboard or users who donate or need blood
ADMIN_USERS = json.loads(os.getenv("ADMIN_USERS", "{}"))

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_TTL = int(os.getenv("REDIS_TTL", 3600))
