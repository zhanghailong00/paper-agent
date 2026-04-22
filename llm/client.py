import os
from pathlib import Path

import openai


def load_env_file(env_path=".env"):
    path = Path(env_path)
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


class LLMClient:
    def __init__(self, api_key, base_url=None, model="gpt-4o-mini"):
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing. Please set it in paper_agent/.env")
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model

    @classmethod
    def from_env(cls, env_path=".env"):
        load_env_file(env_path)
        return cls(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL") or None,
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        )

    def call(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
