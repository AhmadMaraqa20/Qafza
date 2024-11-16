# Jordanian Currency Object Detection API

This project is an object detection API for Jordanian currency. It is built using **FastAPI** for the backend and **Docker** for containerization. The model was trained using Ultralytics and deployed via this API.

## Features
- FastAPI-based backend for currency detection.
- Pretrained YOLO model for object detection.
- Dockerized for easy deployment.

## Files and Folders
- `fastApiPY.py`: FastAPI application.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker configuration for the app.
- `test_Images/`: Sample images for testing.
- `models/`: Contains the YOLO model file.


## How to Use

### DockerHub

You can pull the pre-built Docker image from DockerHub and run it directly. 

To pull the latest image:
```bash
docker pull ahmadmaraqa/fastapi-currency-app:latest
```
Once pulled, you can run the container using:
```bash
docker run -d -p 8000:8000 ahmadmaraqa/fastapi-currency-app:latest
```
This will start the API on port 8000, and you can access it at http://localhost:8000.

For more information, visit the [DockerHub Repository](https://hub.docker.com/repository/docker/ahmadmaraqa/fastapi-currency-app/tags).


### Local Setup

Clone the repository:
```bash
git clone https://github.com/AhmadMaraqa20/Qafza.git
```
Navigate to the project directory:
```bash
cd Qafza
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run the FastAPI application:
```bash
uvicorn fastApiPY:app --reload
```
The application will be accessible at http://localhost:8000.





