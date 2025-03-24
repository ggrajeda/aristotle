import os
import uuid
from dotenv import load_dotenv
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    send_from_directory,
    current_app,
)
from app.services.textbot_service import TextBotService
from app.services.voicebot_service import VoiceBotService

# File with prompt configuring an AI lecturer
_CONFIG_PROMPT_FILE = "prompt.txt"

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


def _get_environment_variable(var_name):
    env_var = os.environ.get(var_name)
    if not env_var:
        raise KeyError(f"{var_name} environment variable is not set")
    return env_var


@main.route("/generate", methods=["POST"])
def generate_lecture():
    # Get topic from request
    topic = request.form.get("topic")
    if not topic or not topic.strip():
        return jsonify({"error": "Topic cannot be empty"}), 400

    static_folder = current_app.static_folder
    assert static_folder != None
    config_path = os.path.join(static_folder, "config", _CONFIG_PROMPT_FILE)

    # Generate a unique filename for this lecture
    lecture_filename = f"{uuid.uuid4()}.wav"
    output_path = os.path.join(static_folder, "audio", lecture_filename)

    try:
        # Initialize services with environment variables
        load_dotenv()
        api_key = _get_environment_variable("LLM_API_KEY")
        api_base_url = _get_environment_variable("LLM_BASE_URL")
        api_model = _get_environment_variable("LLM_MODEL")
        kokoro_voice = _get_environment_variable("KOKORO_VOICE")

        text_bot = TextBotService(
            api_key, api_base_url, api_model, config_path
        )
        voice_bot = VoiceBotService(kokoro_voice, output_path)

        # Generate lecture text
        lecture = text_bot.generate_lecture(topic)

        # Generate lecture audio
        voice_bot.generate_audio(lecture)

        return jsonify(
            {"success": True, "filename": lecture_filename, "text": lecture}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route("/audio/<filename>")
def get_audio(filename):
    static_folder = current_app.static_folder
    assert static_folder != None
    return send_from_directory(os.path.join(static_folder, "audio"), filename)
