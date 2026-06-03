# BIMS FAQ Chatbot API Documentation

## Overview
This is a comprehensive REST API for the BIMS Portal FAQ Chatbot system. The API provides endpoints for querying FAQs, searching, and managing chatbot responses.

## Base URL
```
http://localhost:5000
```

## API Endpoints

### 1. Health Check
**Endpoint:** `GET /api/health`

**Description:** Check if the API is running.

**Response:**
```json
{
    "status": "ok",
    "service": "BIMS FAQ Chatbot API",
    "version": "1.0"
}
```

---

### 2. Service Info
**Endpoint:** `GET /api/info`

**Description:** Get chatbot service information.

**Response:**
```json
{
    "service": "BIMS Portal FAQ Chatbot",
    "version": "1.0",
    "faq_count": 44,
    "status": "active"
}
```

---

### 3. Get Answer (Main Chat Endpoint)
**Endpoint:** `POST /api/chat`

**Description:** Get AI response for a user query.

**Request Body:**
```json
{
    "query": "What is BIMS portal?"
}
```

**Response:**
```json
{
    "answer": "BIMS portal is a platform for final year students to manage, submit, and track their project progress.",
    "confidence": 0.85,
    "question": "What is BIMS portal?",
    "success": true
}
```

---

### 4. Get All FAQs
**Endpoint:** `GET /api/faq`

**Description:** Retrieve all FAQ pairs.

**Response:**
```json
{
    "faq": [
        {
            "question": "What is BIMS portal?",
            "answer": "BIMS portal is a platform for final year students..."
        },
        ...
    ],
    "count": 44
}
```

---

### 5. Search FAQs
**Endpoint:** `POST /api/faq/search`

**Description:** Search FAQs by keyword.

**Request Body:**
```json
{
    "keyword": "upload"
}
```

**Response:**
```json
{
    "keyword": "upload",
    "results": [
        {
            "question": "How to upload project?",
            "answer": "Go to dashboard → click upload → select file → submit."
        },
        {
            "question": "Why is my file not uploading?",
            "answer": "Check file format and size."
        }
    ],
    "count": 2
}
```

---

### 6. FAQ Count
**Endpoint:** `GET /api/faq/count`

**Description:** Get total number of FAQs.

**Response:**
```json
{
    "total_faq": 44
}
```

---

### 7. Legacy Chat Endpoint (Backward Compatible)
**Endpoint:** `POST /chat`

**Description:** Original chat endpoint (maintined for backward compatibility).

**Request Body:**
```json
{
    "query": "How to login?"
}
```

**Response:**
```json
{
    "answer": "You can login using your student or teacher credentials provided by the institution."
}
```

---

## Error Handling

### Missing Query Field
**Status Code:** 400

```json
{
    "error": "Missing 'query' field in request",
    "success": false
}
```

### Server Error
**Status Code:** 500

```json
{
    "error": "Error message here",
    "success": false
}
```

---

## Integration Examples

### cURL
```bash
# Get answer
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "How to upload project?"}'

# Search FAQs
curl -X POST http://localhost:5000/api/faq/search \
  -H "Content-Type: application/json" \
  -d '{"keyword": "deadline"}'

# Get all FAQs
curl -X GET http://localhost:5000/api/faq
```

### Python
```python
import requests

# Get answer
response = requests.post(
    'http://localhost:5000/api/chat',
    json={'query': 'What is BIMS portal?'}
)
print(response.json())

# Search FAQs
response = requests.post(
    'http://localhost:5000/api/faq/search',
    json={'keyword': 'upload'}
)
print(response.json())
```

### JavaScript / Node.js
```javascript
// Get answer
fetch('http://localhost:5000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: 'How to login?' })
})
.then(res => res.json())
.then(data => console.log(data));

// Get all FAQs
fetch('http://localhost:5000/api/faq')
    .then(res => res.json())
    .then(data => console.log(data));
```

---

## Notes

- All endpoints return JSON responses
- POST endpoints require `Content-Type: application/json` header
- The `/api/chat` endpoint is recommended for new integrations
- For production, consider setting `debug=False` in `chatbot.py`
