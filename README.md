# Mimir AI - Agentic Career Intelligence Assistant

Mimir AI is an innovative Agentic AI Career Development Assistant by The Triumvirate team, designed to guide students and early-career professionals from their current skill level to job readiness through continuous analysis, reasoning, and personalized planning.

## Project Overview
This project, developed for the AI-VERSE track by Team The Triumvirate (Team Leader: Ujwal Tatavarthi) at IETE Student Forum, Amrita Vishwa Vidyapeetham, stands out from static career platforms by acting as a self-improving companion that learns from user feedback, job applications, and career history. It reduces uncertainty by explaining failures, identifying skill gaps, and converting effort into measurable progress via adaptive roadmaps.

## Key Features
- **Profile Analyzer**: Extracts skills, experience, and results from resumes.
- **Market Reasoner**: Compares user readiness with job market requirements, identifies skill gaps, and analyzes trends.
- **Planning Module**: Generates personalized skill-building roadmaps, milestones, and application strategies.
- **Persistent Career Memory**: Tracks growth history, events, interviews, and past outcomes using vector databases.
- **Feedback Mechanism**: Learns from rejections, successes, and interviews to refine recommendations.
- **Optimized Recommendations**: Provides tailored job/internship matches and resume customization for specific roles.
- **Progress Summaries**: Delivers weekly career updates.

## How It Works
1. User uploads resume and career preferences.
2. Profile Analyzer processes inputs; Market Reasoner benchmarks against job market.
3. Planning Module creates roadmap; user applies to jobs with AI guidance.
4. Feedback from applications/interviews updates memory, refining future plans in a continuous loop.

## Tech Stack
- Large Language Models (LLMs) for reasoning and planning.
- Natural Language Processing (NLP) for resume/job analysis.
- Embedding models for skill-job matching.
- Vector Databases for memory persistence.
- Agent frameworks: LangChain, LangGraph.
- Backend: FastAPI.

## Architecture
The system features a Coordinator Agent routing tasks across modules: User Interfaces → Profile Analyzer → Market Reasoner → Career Memory → Planning Roadmap → Execution Feedback, with a feedback loop for continuous improvement.

## Getting Started
Clone the repo and set up the environment (detailed setup coming soon). Check the attached PDF ("The_Triumvirate_ver1.pdf") for full project details, diagrams, and process flow.

## Team
- **The Triumvirate** (IETE Student Forum, Amrita Vishwa Vidyapeetham).
- Leader: Ujwal Tatavarthi.

## License
MIT License - feel free to use and contribute!
