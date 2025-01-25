from flask import Flask, request, jsonify    
from flask_cors import CORS  # Import CORS    
from transformers import pipeline    
    
app = Flask(__name__)    
CORS(app)  # Enable CORS for all routes    
    
# Load the GPT-2 model for text generation    
model_name = "gpt2"  # You can choose a different GPT-2 model    
generator = pipeline("text-generation", model=model_name)    
    
def generate_pros_and_cons(tech_stack):    
    # Improved prompt for strengths    
    strength_prompt = f"Considering the technology stack: {tech_stack}, what are the key strengths of using this combination of technologies? Please provide detailed insights."  
    strength_response = generator(strength_prompt, max_length=150, num_return_sequences=1, do_sample=True)    
    pros = strength_response[0]['generated_text'].replace(strength_prompt, "").strip()    
    
    # Improved prompt for weaknesses    
    weakness_prompt = f"Considering the technology stack: {tech_stack}, what are the potential weaknesses or challenges of using this combination of technologies? Please provide detailed insights."  
    weakness_response = generator(weakness_prompt, max_length=150, num_return_sequences=1, do_sample=True)    
    cons = weakness_response[0]['generated_text'].replace(weakness_prompt, "").strip()    
    
    return pros, cons    
    
@app.route('/generate', methods=['POST'])    
def generate():    
    data = request.json    
    frontend = data.get('frontend')    
    backend = data.get('backend')    
    database = data.get('database')    
    
    tech_stack = f"Frontend: {frontend}, Backend: {backend}, Database: {database}"    
        
    # Generate pros and cons    
    pros, cons = generate_pros_and_cons(tech_stack)    
    
    # Improved prompt for summary    
    summary_prompt = f"Please summarize the following technology stack: {tech_stack}. Include key points about its strengths, weaknesses, and overall suitability for web development."  
    summary_response = generator(summary_prompt, max_length=150, num_return_sequences=1, do_sample=True)    
    summary = summary_response[0]['generated_text'].replace(summary_prompt, "").strip()    
    
    return jsonify({    
        'pros': pros,    
        'cons': cons,    
        'summary': summary    
    })    
    
if __name__ == '__main__':    
    app.run(debug=True)    
