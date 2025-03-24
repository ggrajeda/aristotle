from pathlib import Path
import logging
from openai import OpenAI


def _read_contents(filepath: str) -> str:
    with open(filepath, "r") as f:
        contents = f.read()
    return contents


class TextBotService:
    def __init__(
        self, api_key: str, base_url: str, model: str, config_path: str
    ):
        self._api_key = api_key
        self._base_url = base_url
        self._model = model
        self._config_path = config_path

    def _log_response(self, topic: str, response: str) -> None:
        logging.basicConfig(
            filename="textbot.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
        )
        logging.info(f"Topic: {topic}")
        logging.info(f"Response: {response}")

    def generate_lecture(self, topic: str) -> str:
        """Generate lecture script from prompt using OpenAI API"""
        if topic == "test":
            return "Testing, testing. One, two, three!"
        client = OpenAI(
            api_key=self._api_key,
            base_url=self._base_url,
        )
        config_prompt = _read_contents(self._config_path)
        response = client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": config_prompt},
                {"role": "user", "content": topic},
            ],
            stream=False,
        )
        response_content = response.choices[0].message.content
        assert response_content != None
        self._log_response(topic, response_content)
        return response_content
