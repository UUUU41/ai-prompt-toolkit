# 🤖 AI Prompt Toolkit

A practical collection of **15 ready-to-use AI prompt templates** for study, coding and content writing — available in **three formats** in one repository: a readable Markdown collection, a small web app, and a Python command-line tool.

Every template is complete and genuinely useful: copy it, replace the `[BRACKETED]` parts with your own details, and paste it into any AI chat tool (ChatGPT, Claude, Gemini, etc.).

## ✨ What's inside

| File | What it is |
|---|---|
| `prompts.md` | All 15 prompts in one Markdown file — read, copy and paste. |
| `index.html` + `style.css` + `app.js` | A small web app to search, filter and copy the prompts in your browser. |
| `prompt_generator.py` | A Python CLI that asks for your details and builds the finished prompt for you. |

## 📚 The 15 prompts

**Study & Learning**
1. Explain Like I'm a Beginner
2. Feynman Technique Coach
3. Quiz Generator
4. Personal Study Plan
5. Notes Summariser

**Coding & Development**
6. Line-by-Line Code Explainer
7. Bug Finder and Fixer
8. Friendly Code Reviewer
9. Build a Function from a Description
10. Code Language Converter

**Content & Writing**
11. Paragraph Rewriter
12. Blog Post Writer
13. Social Media Caption Generator
14. Professional Email Writer
15. Resume Bullet Improver

## 🚀 How to run each part

### 1. Prompt collection (`prompts.md`)
Simply open `prompts.md`, find the prompt you need, copy the text inside its code block, fill in the `[BRACKETS]`, and paste it into your AI chat tool.

### 2. Web app (`index.html`)
Open `index.html` in any web browser — no server or internet needed.
- 🔍 **Search box** — filters prompts by any word in the title, text or description.
- 🏷️ **Category buttons** — All / Study / Coding / Content.
- 📋 **Copy button** on every card — copies the prompt to your clipboard and shows a "Copied!" confirmation.

### 3. Python CLI (`prompt_generator.py`)
Requires Python 3 (standard library only, nothing to install):

```bash
python3 prompt_generator.py
```

It lists all 15 templates grouped by category, you type a number, answer the questions for each `[PLACEHOLDER]`, and it prints the finished, ready-to-paste prompt. Invalid input (letters instead of numbers, out-of-range choices) is handled gracefully — it simply asks again. Type `q` to quit.

## 🛠️ Tech used
- Markdown for the prompt collection
- Plain HTML, CSS and vanilla JavaScript for the web app (no frameworks, no build step)
- Python 3 standard library for the CLI

## 🔮 Future improvements
- Add more categories (Interview Prep, Business, Language Learning)
- Let the web app fill in placeholders in the browser before copying
- Save favourite prompts in the web app using localStorage
- Add an option in the CLI to save the finished prompt to a text file
- Hindi/Hinglish versions of the most popular prompts

## 👤 Author
**Chandan Yadav** — BCA student, frontend developer and AI prompt engineer from India.
GitHub: [@UUUU41](https://github.com/UUUU41)

## 📄 License
Free to use for learning and personal projects. If you reuse the prompts, a mention of this repository is appreciated.
