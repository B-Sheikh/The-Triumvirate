from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Mock data storage (in production, use a database)
user_data = {
    "profile": {
        "name": "Alex Chen",
        "currentRole": "Computer Science Student",
        "skills": ["Python", "JavaScript", "Data Structures"],
        "targetRole": "Full Stack Developer",
        "experience": "Beginner"
    },
    "roadmap": [
        {
            "id": 1,
            "phase": "Foundation",
            "status": "in-progress",
            "progress": 65,
            "tasks": [
                {"name": "Master React fundamentals", "completed": True, "days": 14},
                {"name": "Build 3 portfolio projects", "completed": False, "days": 30},
                {"name": "Learn REST APIs", "completed": True, "days": 7}
            ]
        },
        {
            "id": 2,
            "phase": "Intermediate Skills",
            "status": "upcoming",
            "progress": 0,
            "tasks": [
                {"name": "Advanced React patterns", "completed": False, "days": 21},
                {"name": "Database design & SQL", "completed": False, "days": 14},
                {"name": "System design basics", "completed": False, "days": 20}
            ]
        },
        {
            "id": 3,
            "phase": "Job Readiness",
            "status": "locked",
            "progress": 0,
            "tasks": [
                {"name": "Technical interview prep", "completed": False, "days": 30},
                {"name": "Build capstone project", "completed": False, "days": 45},
                {"name": "Mock interviews & networking", "completed": False, "days": 20}
            ]
        }
    ],
    "insights": [
        {
            "type": "success",
            "title": "Strong Progress This Week",
            "message": "You completed 3 tasks ahead of schedule. Your learning velocity has increased 40%.",
            "action": "View Analytics"
        },
        {
            "type": "warning",
            "title": "Skill Gap Detected",
            "message": "Based on 250 Full Stack job postings, TypeScript appears in 78% of requirements. Consider adding this to your roadmap.",
            "action": "Adjust Roadmap"
        },
        {
            "type": "info",
            "title": "Market Insight",
            "message": "Companies in your target area are now prioritizing Next.js experience. This trend emerged in the last 2 weeks.",
            "action": "Learn More"
        }
    ],
    "chat_history": [
        {
            "sender": "mimir",
            "text": "Hi Alex! I've analyzed your progress. You're 65% through Foundation phase. Ready to discuss your next steps?",
            "timestamp": datetime.now().isoformat()
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/profile', methods=['GET'])
def get_profile():
    return jsonify(user_data["profile"])

@app.route('/api/roadmap', methods=['GET'])
def get_roadmap():
    return jsonify(user_data["roadmap"])

@app.route('/api/insights', methods=['GET'])
def get_insights():
    return jsonify(user_data["insights"])

@app.route('/api/chat', methods=['GET'])
def get_chat():
    return jsonify(user_data["chat_history"])

@app.route('/api/chat', methods=['POST'])
def post_chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Add user message
    user_data["chat_history"].append({
        "sender": "user",
        "text": user_message,
        "timestamp": datetime.now().isoformat()
    })
    
    # Generate AI response (mock - in production, call Claude API)
    ai_response = generate_ai_response(user_message)
    user_data["chat_history"].append({
        "sender": "mimir",
        "text": ai_response,
        "timestamp": datetime.now().isoformat()
    })
    
    return jsonify(user_data["chat_history"])

def generate_ai_response(message):
    """Mock AI response generator"""
    responses = {
        "help": "I can help you with career planning, skill development, job market insights, and personalized recommendations. What would you like to know?",
        "skills": "Based on your current progress, I recommend focusing on React, Node.js, and database technologies. These are in high demand for Full Stack roles.",
        "jobs": "The job market for Full Stack Developers is strong. Entry-level positions typically require 1-2 years of experience or equivalent portfolio projects.",
        "default": "Based on your current trajectory and the latest job market data, I recommend focusing on building a full-stack project next. This will demonstrate your skills while teaching you backend integration - a combination that's appearing in 65% of entry-level positions."
    }
    
    message_lower = message.lower()
    if "help" in message_lower:
        return responses["help"]
    elif "skill" in message_lower:
        return responses["skills"]
    elif "job" in message_lower:
        return responses["jobs"]
    else:
        return responses["default"]

@app.route('/api/task/complete', methods=['POST'])
def complete_task():
    data = request.json
    phase_id = data.get('phase_id')
    task_name = data.get('task_name')
    
    # Find and update task
    for phase in user_data["roadmap"]:
        if phase["id"] == phase_id:
            for task in phase["tasks"]:
                if task["name"] == task_name:
                    task["completed"] = True
                    # Recalculate progress
                    completed = sum(1 for t in phase["tasks"] if t["completed"])
                    phase["progress"] = int((completed / len(phase["tasks"])) * 100)
                    break
    
    return jsonify({"status": "success", "roadmap": user_data["roadmap"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
