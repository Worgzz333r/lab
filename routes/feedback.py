from flask import Blueprint, render_template, request, jsonify
from models import get_db_connection

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (name, email, subject ,message) VALUES (?, ?, ?, ?)',
                     (name, email, subject, message))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success"}), 200
    
    return render_template('feedback.html')