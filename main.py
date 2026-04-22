from pathlib import Path

from llm.client import LLMClient
from core.pipeline import WritingPipeline


BASE_DIR = Path(__file__).resolve().parent


def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_prompts():
    return {
        "translate": load_prompt(BASE_DIR / "prompts" / "translate.txt"),
        "rewrite": load_prompt(BASE_DIR / "prompts" / "rewrite.txt"),
        "deai": load_prompt(BASE_DIR / "prompts" / "deai.txt"),
        "review": load_prompt(BASE_DIR / "prompts" / "review.txt"),
    }


def save_output(result):
    output_dir = BASE_DIR / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_dir / "result.txt", "w", encoding="utf-8") as f:
        for k, v in result.items():
            f.write(f"\n===== {k.upper()} =====\n")
            f.write(v + "\n")


if __name__ == "__main__":
    llm = LLMClient.from_env(BASE_DIR / ".env")
    prompts = load_prompts()

    pipeline = WritingPipeline(llm, prompts)

    text = input("请输入中文草稿：\n")

    result = pipeline.run(text)

    save_output(result)

    print("\n已生成结果，查看 paper_agent/outputs/result.txt")
