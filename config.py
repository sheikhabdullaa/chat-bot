# BIMS Chatbot Configuration

API_CONFIG = {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": True,
    "similarity_threshold": 0.05,
}

# CORS Configuration (for production integration with other services)
CORS_CONFIG = {
    "allow_credentials": True,
    "allow_methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"],
    "max_age": 3600
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
}
