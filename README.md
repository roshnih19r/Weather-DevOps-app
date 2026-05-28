# Weather DevOps App

A Flask-based Weather Application 
deployed with complete DevOps pipeline.

## Tech Stack
- **App:** Python Flask
- **Container:** Docker
- **CI/CD:** Jenkins
- **Cloud:** AWS EC2
- **API:** OpenWeatherMap

## Features
- Real-time weather data
- Dockerized application
- Automated CI/CD pipeline
- Live on AWS EC2

## Project Structure

weather-devops-app/
├── app/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   └── routes.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── run.py

## Live Demo
http://3.111.227.72:5000

## CI/CD Pipeline
1. Code push to GitHub
2. Jenkins auto trigger
3. Docker image build
4. Deploy to EC2
