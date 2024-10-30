from flask import Flask, request, render_template, jsonify, redirect, url_for  # Added imports for redirect and url_for
import os
import logging
import gemini  # Ensure you have a 'generate_response' function in gemini.py
import llama  # Ensure you have a 'generate_response' function in llama.py
import streamlit as st

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# File path for visitor count tracking
counter_file_path = 'visitor_count.txt'

# Function to get the current visitor count from a file
def get_visitor_count():
    if not os.path.exists(counter_file_path):
        with open(counter_file_path, 'w') as file:
            file.write('0')
    with open(counter_file_path, 'r') as file:
        count = int(file.read())
    return count

# Function to increment the visitor count
def increment_visitor_count():
    count = get_visitor_count()
    count += 1
    with open(counter_file_path, 'w') as file:
        file.write(str(count))
    return count

# Route for the landing page that tracks visitor count
@app.route('/')
def landing():
    visitor_count = increment_visitor_count()
    return render_template('index.html', visitor_count=visitor_count)

# Route to render the chat page
@app.route('/chat_page')
def chat_page():
    return render_template('chat_page.html')

# Route for login; redirect to the chat page after "logging in"
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Implement authentication logic here (e.g., database check)
    return redirect(url_for('chat_page'))

# Route for signup; redirect to the chat page after "signing up"
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    # Implement signup logic here (e.g., save to database)
    return redirect(url_for('chat_page'))

# Route to handle user input and get responses from Llama and Gemini
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            raise ValueError("No message provided in request.")

        # Get responses from both Llama and Gemini models
        llama_response = llama.generate_response(user_input)
        gemini_response = gemini.generate_response(user_input)

        # Prepare the combined response
        combined_response = {
            'llama': llama_response,
            'gemini': gemini_response
        }

        return jsonify(combined_response)
    except Exception as e:
        logging.error(f"Error in get_response: {e}")
        return jsonify({'response': f'An error occurred: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
