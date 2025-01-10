import os # for file and directory management
from flask import Flask, request, jsonify, render_template # web framework (like React)


# Create a Flask app
app = Flask(__name__)

# Reads a text file and converts its content into a dictionary.
def process_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
    
    feedback_dict = {}
    # Loop through each line and split it into key-value pairs
    for line in lines:
        key, value = line.strip().split(": ", 1)
        feedback_dict[key] = value
    
    return feedback_dict



@app.route('/')
def home():
    """
    Displays the homepage with a list of feedback files.
    It reads files from the 'data/feedback' folder and passes them to the template.
    """
    feedback_dir = 'data/feedback'  # Directory where feedback files are stored
    files = os.listdir(feedback_dir)  # Get a list of all files in the folder
    return render_template('index.html', files=files)  # Pass files to the HTML template


@app.route('/process-feedback/<filename>', methods=['GET'])
def process_feedback(filename):
    """
    Handles requests to process a specific feedback file.
    Converts the file content into a dictionary and returns it as JSON.
    """
    feedback_dir = 'data/feedback'  # Folder with feedback files
    file_path = os.path.join(feedback_dir, filename)  # Full path to the file
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return {"error": "File not found"}, 404  # Return error if file doesn't exist
    
    try:
        # Process the file and return its content as JSON
        feedback_dict = process_file(file_path)
        return jsonify(feedback_dict), 200
    except Exception as e:
        # Handle any errors during file processing
        return {"error": str(e)}, 500



if __name__ == '__main__':
    # Make sure the 'data/feedback' directory exists
    os.makedirs('data/feedback', exist_ok=True)
    # Run the app in debug mode for easier testing and troubleshooting
    app.run(debug=True)
