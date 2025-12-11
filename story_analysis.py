mport litellm
import json
from typing import Dict

def call_llm(model: str, system_prompt: str, user_prompt: str) -> str:
    """
    Wrapper for LiteLLM chat completion.
    """
    response = litellm.completion(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]


def generate_summary(story: str, model: str) -> str:
    system_prompt = "You are an expert literary analyst who writes concise, accurate summaries."
    user_prompt = f"Write a 250-word summary of the following story:\n\n{story}"
    return call_llm(model, system_prompt, user_prompt)


def generate_moral(story: str, model: str) -> str:
    system_prompt = "You are a literary critic who identifies the thematic moral lessons in narratives."
    user_prompt = f"Explain the moral(s) of the following story:\n\n{story}"
    return call_llm(model, system_prompt, user_prompt)


def generate_critique(story: str, model: str) -> str:
    system_prompt = "You are a professional literature reviewer. Provide a balanced critique of the story."
    user_prompt = f"Critique the following story, discussing strengths, weaknesses, narrative choices, and emotional impact:\n\n{story}"
    return call_llm(model, system_prompt, user_prompt)


def generate_analysis(story: str, model: str) -> str:
    system_prompt = "You are an academic literary analyst. Provide deep structural, thematic, and stylistic analysis."
    user_prompt = f"Provide a detailed analysis of the following story. Include themes, character psychology, symbolism, narrative structure, and social context:\n\n{story}"
    return call_llm(model, system_prompt, user_prompt)


def analyze_story(story: str, model: str) -> Dict[str, str]:
    """
    Main function that returns a dictionary containing all outputs.
    """
    return {
        "summary": generate_summary(story, model),
        "moral": generate_moral(story, model),
        "critique": generate_critique(story, model),
        "analysis": generate_analysis(story, model)
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="LiteLLM Story Analyzer")
    parser.add_argument("--story_file", type=str, required=True, help="Path to text file containing the story")
    parser.add_argument("--model", type=str, required=True, help="Model name for LiteLLM (e.g. 'gpt-4o', 'gemini/gemini-1.5-flash')")

    args = parser.parse_args()

    # Load story
    with open(args.story_file, "r", encoding="utf-8") as f:
        story_text = f.read()

    # Run analysis
    result = analyze_story(story_text, args.model)

    # Print nicely formatted JSON
    print(json.dumps(result, indent=4, ensure_ascii=False))

