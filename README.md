# BIMS FAQ AI Chatbot

This is an AI-powered FAQ chatbot for the BIMS portal with a comprehensive REST API for easy integration.

## Features
- **Smart FAQ Matching:** Uses TF-IDF vectorization for accurate Q&A matching
- **Web Interface:** Modern chat UI with typing animations
- **REST API:** Multiple endpoints for easy integration with other systems
- **Search:** Full-text search across FAQ database
- **Extensible:** Easy to add more Q&A pairs
- **Production Ready:** Error handling, logging, configuration

## Quick Start

### 1. Environment Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Chatbot
```bash
python chatbot.py
```

The application will start on `http://localhost:5000`

### 3. Access
- **Web UI:** `http://localhost:5000/`
- **API Base:** `http://localhost:5000/api/`

## Project Structure
```
FAQ AI/
├── chatbot.py              # Main Flask app with API endpoints
├── chatbot_service.py      # Core chatbot logic service
├── qa_data.py              # FAQ dataset (44 Q&A pairs)
├── config.py               # Configuration settings
├── test_api.py             # API testing script
├── requirements.txt        # Python dependencies
├── API_DOCUMENTATION.md    # Complete API reference
├── static/index.html       # Web UI (chat interface)
└── README.md               # This file
```

## API Endpoints

### Health & Info
- `GET /api/health` - Check API status
- `GET /api/info` - Get service information
- `GET /api/faq/count` - Get FAQ total count

### Chat & FAQ
- `POST /api/chat` - Get AI response (with confidence score)
- `GET /api/faq` - Get all FAQ pairs
- `POST /api/faq/search` - Search FAQs by keyword

### Legacy
- `POST /chat` - Original endpoint (backward compatible)

## Usage Examples

### cURL
```bash
# Get an answer
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "How to upload project?"}'
```

### Python
```python
import requests

response = requests.post(
    'http://localhost:5000/api/chat',
    json={'query': 'What is BIMS portal?'}
)
print(response.json())
```

### JavaScript
```javascript
fetch('http://localhost:5000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: 'How to login?' })
})
.then(res => res.json())
.then(data => console.log(data));
```

## Testing

Run the API test suite:
```bash
python test_api.py
```

This will test all endpoints and show sample responses.

## Training Data

Currently trained on 44 BIMS portal FAQ pairs covering:
- Student dashboard & uploads
- Progress tracking
- Teacher features
- Deadlines & tasks
- Resubmission
- Support & help

## Configuration

Edit `config.py` to customize:
- API host/port
- Similarity threshold
- CORS settings
- Logging level

## Integration Guide

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete integration instructions and examples.

## Requirements
- Python 3.8+
- Flask
- scikit-learn
- nltk

## Future Enhancements
- Add database support
- User authentication
- Chat history logging
- Admin panel for FAQ management
- Multi-language support
