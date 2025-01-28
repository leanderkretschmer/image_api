# Image API with LocalAI Integration #

This project provides a lightweight API that receives images via HTTP requests, stores them locally, and forwards them to a LocalAI instance for further processing. The project is containerized using Docker and designed to run seamlessly alongside a LocalAI service.

## Features
- Accepts images through an API endpoint.
- Saves images locally with a timestamp-based filename.
- Forwards the image to a LocalAI instance for processing.
- Fully containerized for easy deployment.

---

## Project Structure
```
.
├── docker-compose.image-api.yml  # Compose file for the Image API
├── image-api                     # Image API application code
│   ├── app.py                   # Main Flask application
│   ├── Dockerfile               # Dockerfile to build the Image API service
│   ├── requirements.txt         # Python dependencies
├── storage                       # Local storage for saved images
```

---

## Prerequisites
- Docker and Docker Compose installed.
- A running LocalAI instance.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/leanderkretschmer/image_api
   cd <your-repo>
   ```

2. Start the services:
   ```bash
   docker-compose -f docker-compose.image-api.yml up -d
   ```

3. Verify that the Image API is running:
   - API URL: `http://localhost:5000`

4. Ensure that LocalAI is running and accessible at the `LOCALAI_API_URL` provided in the environment variables.

---

## Usage

### Uploading an Image
You can upload an image to the API using `curl` or any HTTP client:
```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/upload
```

### Response
- **Success**:
  ```json
  {
    "message": "Image saved and forwarded",
    "localai_response": { ... }
  }
  ```
- **Error**:
  ```json
  {
    "error": "Error details"
  }
  ```

---

## Environment Variables

- `LOCALAI_API_URL`: URL to the LocalAI instance (default: `http://localai:8080/v1/images`)

---

## Volumes

- `./storage`: Maps to the container's `/storage` directory where images are saved locally.

---

## Local Development

1. Install dependencies:
   ```bash
   pip install -r image-api/requirements.txt
   ```

2. Run the Flask app:
   ```bash
   python image-api/app.py
   ```

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the Oracle License. For more details, please refer to the [Oracle License Agreement](https://www.oracle.com/legal/) 
