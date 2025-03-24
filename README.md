# Aristotle

Generate lecture audio from a prompt using AI

## Setup

Before you get started, make sure
[Docker](https://docs.docker.com/get-started/get-docker/) is installed on your
machine.

To run the web application: 
1. Clone the repository using `git clone https://github.com/ggrajeda/aristotle`

2. Copy `.env.example` to `.env`:
   ```
   cp .env.example .env
   ```

3. Edit the `.env` file with your preferred settings:
   - `LLM_API_KEY`: API key for your favorite LLM service
   - `LLM_BASE_URL`: API endpoint (e.g., `https://api.anthropic.com/v1/`)
   - `LLM_MODEL`: LLM model name (e.g., `claude-3-7-sonnet-20250219`)
   - `KOKORO_VOICE`: Kokoro voice to use for audio generation (e.g., `af_heart`)

4. Build and run the Docker container inside the project directory:
   ```
   docker-compose up --build
   ```

5. Access the application at http://localhost:8080
