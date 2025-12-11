# Story Analysis

A tool for analyzing stories using language models. This project provides utilities to generate summaries, extract morals, provide critiques, and analyze story structure using any LLM via LiteLLM.

## Features

- **Story Collection Management**: Organize and analyze multiple stories
- **LLM-Based Analysis**: Use any LLM to analyze stories
  - **Summaries**: Generate summaries
  - **Moral Extraction**: Identify themes and lessons
  - **Critique**: Generate literary criticism with strengths and weaknesses
  - **Analysis**: Extract themes, symbolism, narrative structure, and social context
- **Word Count Utility**: Count words across story files
- **LLM Support**: Compatible with GPT-4, Claude, Gemini, and other LiteLLM-supported models

## Project Structure

```
StoryAnalysis/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── story_analysis.py            # Main story analysis script
├── WordCount.py                 # Word counting utility
└── stories/
    ├── [PDF versions]
    └── txt/
        └── [Story text files]
```

## Installation

### Prerequisites
- Python 3.8 or higher
- An API key for your chosen LLM provider (OpenAI, Anthropic, Google, etc.)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/csv610/StoryAnalysis.git
cd StoryAnalysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your LLM API key:
```bash
export OPENAI_API_KEY="your-key-here"  # Or your provider's equivalent
```

## Usage

### Story Analysis

Analyze any story using your chosen LLM:

```bash
python story_analysis.py \
  --story_file stories/txt/your_story.txt \
  --model gpt-4o
```

Supported models (via LiteLLM):
- `gpt-4o`, `gpt-4-turbo` (OpenAI)
- `claude-opus`, `claude-sonnet` (Anthropic)
- `gemini/gemini-1.5-pro`, `gemini/gemini-1.5-flash` (Google)
- And many more LiteLLM-supported models

**Output**: JSON-formatted analysis with summary, moral, critique, and detailed analysis.

Example output:
```json
{
    "summary": "A concise summary of the story...",
    "moral": "The moral lesson or theme of the story...",
    "critique": "A balanced literary critique including strengths and weaknesses...",
    "analysis": "Deep structural, thematic, and stylistic analysis..."
}
```

### Word Count Analysis

Count words in stories to understand their length:

```bash
# Single file
python stories/txt/WordCount.py stories/txt/your_story.txt

# All stories in directory
python stories/txt/WordCount.py stories/txt/
```

## Dependencies

- **litellm**: Unified API for multiple LLM providers
- Python standard library (os, glob, json, argparse)

See `requirements.txt` for exact versions.

## How It Works

### Analysis Pipeline

1. Load the story text from a file
2. Send the text to your chosen LLM with task-specific prompts:
   - System prompt: Defines the LLM's role (literary analyst, critic, etc.)
   - User prompt: Contains the task and story text
3. Parse and format the response as JSON
4. Output results to stdout

### Analysis Features

This approach provides:
- Multiple analytical frameworks (structural, thematic, symbolic)
- Analysis results from different models and prompts
- Ability to process multiple stories

## Configuration

Edit `story_analysis.py` to customize:
- Summary length
- Analysis depth and focus areas
- Additional analysis types
- Prompt engineering for specific domains

## Performance Notes

- First run may be slower due to API initialization
- Analysis time depends on story length and LLM response time
- Typical analysis takes 5-30 seconds depending on model

## Common Issues

**API Key Not Found**: Ensure your environment variable is set correctly
```bash
echo $OPENAI_API_KEY  # Should output your key
```

**Connection Error**: Check internet connectivity and API service status

**Model Not Available**: Verify the model name is spelled correctly and supported by your LiteLLM configuration

## Contributing

To contribute:
- Add new analysis types
- Improve prompts
- Add support for more file formats
- Fix bugs or improve documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [LiteLLM Documentation](https://docs.litellm.ai/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
