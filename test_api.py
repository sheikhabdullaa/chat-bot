"""
API Testing and Demo Script
Run this script to test all API endpoints
"""

import requests
import json
from colorama import Fore, Style, init

init()  # Initialize colorama

BASE_URL = "http://localhost:5000"

def print_header(title):
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{title}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

def print_success(msg):
    print(f"{Fore.GREEN}✓ {msg}{Style.RESET_ALL}")

def print_error(msg):
    print(f"{Fore.RED}✗ {msg}{Style.RESET_ALL}")

def print_json(data):
    print(f"{Fore.YELLOW}{json.dumps(data, indent=2)}{Style.RESET_ALL}")

def test_health():
    print_header("1. Testing Health Check")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print_success("Health check passed")
        print_json(response.json())
    except Exception as e:
        print_error(f"Health check failed: {e}")

def test_service_info():
    print_header("2. Testing Service Info")
    try:
        response = requests.get(f"{BASE_URL}/api/info")
        print_success("Service info retrieved")
        print_json(response.json())
    except Exception as e:
        print_error(f"Service info failed: {e}")

def test_chat():
    print_header("3. Testing Chat API")
    test_queries = [
        "What is BIMS portal?",
        "How to upload project?",
        "How do I view teacher feedback?"
    ]
    
    for query in test_queries:
        try:
            response = requests.post(
                f"{BASE_URL}/api/chat",
                json={"query": query}
            )
            print_success(f"Query: {query}")
            print_json(response.json())
        except Exception as e:
            print_error(f"Chat failed for '{query}': {e}")

def test_all_faq():
    print_header("4. Testing Get All FAQs")
    try:
        response = requests.get(f"{BASE_URL}/api/faq")
        data = response.json()
        print_success(f"Retrieved {data['count']} FAQs")
        print(f"{Fore.YELLOW}First 3 FAQs:{Style.RESET_ALL}")
        for faq in data['faq'][:3]:
            print(f"  Q: {faq['question']}")
            print(f"  A: {faq['answer']}\n")
    except Exception as e:
        print_error(f"Get FAQs failed: {e}")

def test_search_faq():
    print_header("5. Testing Search FAQs")
    keywords = ["upload", "deadline", "teacher"]
    
    for keyword in keywords:
        try:
            response = requests.post(
                f"{BASE_URL}/api/faq/search",
                json={"keyword": keyword}
            )
            data = response.json()
            print_success(f"Search for '{keyword}' - Found {data['count']} results")
            for result in data['results']:
                print(f"  Q: {result['question']}")
        except Exception as e:
            print_error(f"Search failed for '{keyword}': {e}")

def test_faq_count():
    print_header("6. Testing FAQ Count")
    try:
        response = requests.get(f"{BASE_URL}/api/faq/count")
        print_success("FAQ count retrieved")
        print_json(response.json())
    except Exception as e:
        print_error(f"FAQ count failed: {e}")

def test_legacy_endpoint():
    print_header("7. Testing Legacy /chat Endpoint")
    try:
        response = requests.post(
            f"{BASE_URL}/chat",
            json={"query": "Can I resubmit my work?"}
        )
        print_success("Legacy endpoint works")
        print_json(response.json())
    except Exception as e:
        print_error(f"Legacy endpoint failed: {e}")

def main():
    print(f"\n{Fore.MAGENTA}BIMS FAQ Chatbot API - Test Suite{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Base URL: {BASE_URL}{Style.RESET_ALL}")
    
    try:
        test_health()
        test_service_info()
        test_chat()
        test_all_faq()
        test_search_faq()
        test_faq_count()
        test_legacy_endpoint()
        
        print_header("✓ All Tests Completed!")
        print(f"{Fore.GREEN}API is ready for integration!{Style.RESET_ALL}\n")
    
    except Exception as e:
        print_error(f"Critical error: {e}")

if __name__ == "__main__":
    main()
