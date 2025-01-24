from flask import Flask, request, jsonify  
from flask_cors import CORS  # Import CORS  
from transformers import pipeline  
  
app = Flask(__name__)  
CORS(app)  # Enable CORS for all routes  
  
# Load the Hugging Face model for text generation  
model_name = "facebook/bart-large-cnn"  # You can choose a different model  
summarizer = pipeline("summarization", model=model_name)  
  
def generate_pros_and_cons(tech_stack):  
    # Here you can define your logic to generate pros and cons  
    pros = f"Pros of using {tech_stack}: Efficient, Scalable, Popular."  
    cons = f"Cons of using {tech_stack}: Steep learning curve, Requires maintenance."  
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
  
    # Generate summary using the summarization model  
    summary = summarizer(tech_stack, max_length=100, min_length=50, do_sample=False)  
  
    return jsonify({  
        'pros': pros,  
        'cons': cons,  
        'summary': summary[0]['summary_text']  
    })  
  
if __name__ == '__main__':  
    app.run(debug=True)  
