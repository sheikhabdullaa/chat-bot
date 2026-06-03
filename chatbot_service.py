# import re
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from qa_data import qa_pairs


# class BIMSChatbotService:
#     """BIMS FAQ Chatbot Service - Handles all chatbot logic and inference."""
    
#     def __init__(self):
#         self.qa_pairs = qa_pairs
#         self.questions = [pair['question'] for pair in qa_pairs]
#         self.answers = [pair['answer'] for pair in qa_pairs]
#         # Keep all tokens (don't remove English stop words) so short questions
#         # like "what is my name" retain meaningful tokens such as "name".
#         self.vectorizer = TfidfVectorizer(stop_words=None)
#         self.tfidf_matrix = self.vectorizer.fit_transform([q.lower() for q in self.questions])
#         self.similarity_threshold = 0.05
    
#     @staticmethod
#     def preprocess(text):
#         """Preprocess query text for better matching."""
#         text = text.lower()
#         text = re.sub(r'[^a-z0-9\s]', ' ', text)
#         text = re.sub(r'\s+', ' ', text).strip()
#         return text
    
#     def get_answer(self, query):
#         """Get the best answer for a given query."""
#         if not query or not query.strip():
#             return "Please ask a valid question."
        
#         query_processed = self.preprocess(query)
#         query_vec = self.vectorizer.transform([query_processed])
#         similarities = cosine_similarity(query_vec, self.tfidf_matrix)
#         best_match_idx = similarities.argmax()
#         best_score = similarities[0][best_match_idx]
        
#         if best_score > self.similarity_threshold:
#             return {
#                 "answer": self.answers[best_match_idx],
#                 "confidence": float(best_score),
#                 "question": self.questions[best_match_idx],
#                 "success": True
#             }
#         return {
#             "answer": "Sorry, I don't understand that question. Please ask a BIMS portal question.",
#             "confidence": 0.0,
#             "question": None,
#             "success": False
#         }
    
#     def get_all_faq(self):
#         """Return all FAQ pairs."""
#         return self.qa_pairs
    
#     def search_faq(self, keyword):
#         """Search FAQ by keyword."""
#         keyword_lower = keyword.lower()
#         results = [
#             pair for pair in self.qa_pairs 
#             if keyword_lower in pair['question'].lower() or keyword_lower in pair['answer'].lower()
#         ]
#         return results
    
#     def get_faq_count(self):
#         """Return total count of FAQ pairs."""
#         return len(self.qa_pairs)
    
#     def get_service_info(self):
#         """Return service information."""
#         return {
#             "service": "BIMS Portal FAQ Chatbot",
#             "version": "1.0",
#             "faq_count": self.get_faq_count(),
#             "status": "active"
#         }

from flask import Flask, request, jsonify
from flask_cors import CORS

from chatbot import BIMSChatbotService

app = Flask(__name__)
CORS(app)

chatbot = BIMSChatbotService()


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        query = data.get("query", "")

        response = chatbot.get_answer(query)

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "answer": "Server error",
            "success": False,
            "error": str(e)
        }), 500


@app.route('/')
def home():
    return "BIMS Chatbot Server Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)