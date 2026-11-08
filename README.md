# AI Prompt Toolkit

A collection of useful AI prompt templates for study, coding and content creation.

## Features

- Ready-to-copy prompt templates for study, coding and content creation
- Prompts organised by category in `prompts.md`, so you can find one fast
- Every prompt has placeholders such as [TOPIC] and [LANGUAGE] to fill in
- A small Python helper, `prompt_generator.py`, that lists prompts and fills in the placeholders for you
- Tips on writing better prompts: give context, set a role and ask for a format
- No sign-up, no API key and no cost - the templates work with any AI chat tool

## Tech Stack

- Markdown - the prompt collection in `prompts.md`
- Python 3 - the `prompt_generator.py` helper (standard library only)
- Works with any AI assistant: ChatGPT, Claude, Gemini, Copilot and others

## How to Run / Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/UUUU41/ai-prompt-toolkit.git
   cd ai-prompt-toolkit
   ```

2. Browse the templates in `prompts.md`, copy one, replace the [PLACEHOLDERS] with your own details, and paste it into your AI chat tool.

3. Or use the helper to pick and fill a prompt:

   ```bash
   python3 prompt_generator.py
   ```

   Choose a category, choose a prompt, then answer the questions for each placeholder. The helper prints the finished prompt, ready to copy.

## Project Structure

```text
ai-prompt-toolkit/
- prompts.md            (prompt templates for study, coding and content)
- prompt_generator.py  (CLI helper to choose and fill in a prompt)
- README.md            (project documentation)
```

## Future Improvements

- Add prompts for job applications, emails and presentations
- Add a simple web page to browse, search and copy prompts
- Add prompts in more languages
- Add a rating system for the most useful prompts
- Add example outputs for each prompt

## Author

Chandan Yadav (UUUU41) - https://github.com/UUUU41
