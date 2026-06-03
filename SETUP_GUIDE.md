# BIMS Chatbot - Step by Step Setup Guide

## Setup Instructions (For Others to Run)

### Step 1: Download/Get the Project Files
- Get the folder: `FAQ AI`
- Make sure you have all these files:
  ```
  chatbot.py
  chatbot_service.py
  qa_data.py
  config.py
  requirements.txt
  static/index.html
  ```

### Step 2: Install Python
- Download Python 3.8+ from: https://www.python.org/downloads/
- During installation, CHECK the box "Add Python to PATH"
- Click Install

### Step 3: Open Command Prompt
- Press `Win + R`
- Type `cmd` and press Enter
- You should see the black terminal window

### Step 4: Navigate to Project Folder
```bash
cd "C:\Users\fahad\Downloads\Python Projects\FAQ AI"
```
*(Replace the path if your folder is in a different location)*

### Step 5: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 6: Install Requirements
Copy-paste this command:
```bash
pip install -r requirements.txt
```

Wait for it to finish (you'll see "Successfully installed..." message)

### Step 7: Run the Chatbot
```bash
python chatbot.py
```

You should see something like:
```
WARNING in app.run()
 * Running on http://127.0.0.1:5000
```

### Step 8: Open in Browser
- Open Google Chrome or any browser
- Go to: `http://localhost:5000`
- You should see the BIMS Chat interface

### Step 9: Test the Chatbot
- Type a question like: "What is BIMS portal?"
- Click Send or press Enter
- Wait for the AI typing animation
- You should get an answer!

---

## Common Issues & Solutions

### Issue: "Python not found"
**Solution:**
- Python not installed or not in PATH
- Reinstall Python and make sure "Add to PATH" is checked

### Issue: "Module not found" or "No module named 'flask'"
**Solution:**
- Run: `pip install -r requirements.txt` again
- Make sure you're in the right folder

### Issue: "Port 5000 already in use"
**Solution:**
- Close other apps using port 5000
- Or change port in `chatbot.py` line: `app.run(debug=True, port=5001)`

### Issue: Browser shows "Cannot reach localhost:5000"
**Solution:**
- Make sure you ran `python chatbot.py` successfully
- Wait 5 seconds for server to start
- Try refreshing the page

---

## Using the API (For Developers)

If integrating with other apps, use these endpoints:

### Basic Chat
```
POST http://localhost:5000/api/chat
Body: {"query": "Your question here"}
```

### Get All FAQs
```
GET http://localhost:5000/api/faq
```

### Search FAQs
```
POST http://localhost:5000/api/faq/search
Body: {"keyword": "upload"}
```

See `API_DOCUMENTATION.md` for full details.

---

## Stopping the Server

In the Command Prompt terminal, press: `Ctrl + C`

---

## For Different Platforms

### Windows (Above)
✓ See steps above

### Mac/Linux
```bash
# Navigate to folder
cd /path/to/FAQ\ AI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run
python3 chatbot.py
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Start server | `python chatbot.py` |
| Stop server | `Ctrl + C` |
| Access web UI | Browse to `http://localhost:5000` |
| Test API | See `API_DOCUMENTATION.md` |
| Install packages | `pip install -r requirements.txt` |
| Activate virtual env | `venv\Scripts\activate` (Windows) |

---

## Need Help?

If something doesn't work:
1. Check if Python is installed: `python --version`
2. Check if in correct folder: `dir` (should show all project files)
3. Try reinstalling requirements: `pip install -r requirements.txt --force-reinstall`
4. Check if port 5000 is free

---

## Next Steps

After it's running:
- Try different questions
- Check the API endpoints
- Integrate with your main BIMS portal
- Add more FAQ entries to `qa_data.py`
