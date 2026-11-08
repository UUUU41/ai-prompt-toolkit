"""AI Prompt Toolkit - pick a prompt template and fill in its placeholders.

Run:  python3 prompt_generator.py
"""

import re

# (category, title, template) - the same prompts as in prompts.md
PROMPTS = [
    ("Study", "Explain Simply",
     "Explain [TOPIC] to me as if I am a [LEVEL]. Use simple language, one everyday "
     "example, and finish with 3 quick questions to test my understanding."),
    ("Study", "Make a Study Plan",
     "I have [NUMBER] days to prepare for [EXAM/TOPIC]. I can study [HOURS] hours "
     "a day. Make a day-by-day study plan with topics, short revision tasks and one "
     "practice test each week."),
    ("Study", "Quiz Me",
     "Quiz me on [TOPIC]. Ask one question at a time, wait for my answer, then tell "
     "me if I was right and explain the correct answer before asking the next question."),
    ("Coding", "Explain Code",
     "Explain what this [LANGUAGE] code does, line by line, in simple terms:\n\n[CODE]"),
    ("Coding", "Debug an Error",
     "I am getting this error in [LANGUAGE]:\n\n[ERROR]\n\nExplain what is causing "
     "the error and show the fixed code."),
    ("Coding", "Write a Function",
     "Write a [LANGUAGE] function that [TASK]. It should take [INPUTS] and return "
     "[OUTPUT]. Add comments explaining each step and give 2 example uses."),
    ("Coding", "Learn a Concept",
     "Teach me [CONCEPT] in [LANGUAGE]. Start with a simple explanation, then show "
     "a short working example, then give me a small exercise to try myself."),
    ("Content", "Brainstorm Ideas",
     "Give me 10 ideas for [TYPE OF CONTENT] about [TOPIC]. The audience is "
     "[AUDIENCE]. For each idea, add a one-line description and a catchy title."),
    ("Content", "Write a Draft",
     "Write a [LENGTH] [TYPE OF CONTENT] about [TOPIC] for [AUDIENCE]. Use a "
     "friendly tone, short paragraphs and a clear heading structure."),
    ("Content", "Social Media Captions",
     "Write 5 short captions for [PLATFORM] about [TOPIC]. Make them friendly, add "
     "one relevant hashtag each, and end one of them with a question to encourage replies."),
]


def fill_template(template):
    """Ask the user for each [PLACEHOLDER] and return the filled prompt."""
    placeholders = sorted(set(re.findall(r"\[([^\]]+)\]", template)))
    filled = template
    for name in placeholders:
        value = input(f"{name}: ").strip()
        filled = filled.replace(f"[{name}]", value)
    return filled


def choose(options, label):
    print(f"\n{label}")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("Choose a number: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print(f"Please enter a number from 1 to {len(options)}.")


def main():
    print("AI Prompt Toolkit")
    categories = sorted({category for category, _, _ in PROMPTS})
    category = choose(categories, "Choose a category:")
    in_category = [p for p in PROMPTS if p[0] == category]
    titles = [title for _, title, _ in in_category]
    title = choose(titles, f"Choose a prompt ({category}):")
    template = next(tmpl for _, t, tmpl in in_category if t == title)
    print("\nFill in the placeholders (press Enter to leave one blank):")
    finished = fill_template(template)
    print("\n--- Your prompt (copy and paste it into your AI chat tool) ---\n")
    print(finished)


if __name__ == "__main__":
    main()
