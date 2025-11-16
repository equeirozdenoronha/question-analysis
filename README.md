## Description

This project analyzes quiz questions by splitting them into two groups based on how many students answered each question correctly:
- **Low scoring questions:** Fewer than 50% of students answered correctly.
- **High scoring questions:** More than 50% of students answered correctly.

For each group, the script finds:
- The most frequent meaningful single words in the questions (excluding stopwords).
- The most common full question texts (treated as "phrases").

All results are saved in both `output.json` and `output.csv`:
- `output.json` includes:
  - `most_common_low_percentage_words`: Top words in low scoring questions.
  - `most_common_high_percentage_words`: Top words in high scoring questions.
  - `most_common_low_percentage_phrases`: Top full question texts in low scoring questions.
  - `most_common_high_percentage_phrases`: Top full question texts in high scoring questions.
- `output.csv` contains two tables:
  - "Most Common Words in Low Scoring Questions"
  - "Most Common Words in High Scoring Questions"
  Each table lists the most frequent words and their number of occurrences.

### How to Use

1. Ensure Python 3 is installed.
2. Place both `quiz_questions.json` and `analysis.py` in the same directory.
3. Run the script with:
   ```
   python analysis.py
   ```
4. Results will be generated in both `output.json` and `output.csv` in the same folder.

The outputs show which words and phrases are most common in high and low scoring groups, helping you compare the language and patterns found in different sets of quiz questions.
