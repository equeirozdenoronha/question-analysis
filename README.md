## Newsela Quiz Question Analysis

### Overview
This project analyzes quiz questions to answer: **What words appear more frequently in questions that students tend to do poorly on vs. questions they do well on?**

### Approach
Questions are separated into two groups based on student performance:
- **Low-scoring questions:** < 50% of students answered correctly (students struggle)
- **High-scoring questions:** > 50% of students answered correctly (students do well)

For each word, we calculate:
- Frequency per 1000 words in each group (normalized to account for different group sizes)
- Difference between groups to identify distinctive words

### Key Findings

**Words more frequent in LOW-scoring questions (students struggle):**
- `paragraph` (+7.15 per 1000) - Questions asking about specific paragraphs
- `select` (+5.15) - Questions requiring selection/identification
- `best` (+4.52) - Questions asking for "best" answer/evidence
- `author` (+1.91) - Questions about author's purpose or intent
- `idea` (+1.63) - Questions about main/central ideas

**Words more frequent in HIGH-scoring questions (students do well):**
- `sentence` (-4.30 per 1000) - Questions about specific sentences
- `word` (-3.77) - Questions about word meaning/usage  
- `according` (-3.35) - Direct factual recall questions
- `read` (-1.70) - Questions with sentence reading prompts
- `above` (-1.61) - Questions referencing specific content

### Interpretation
Students struggle more with questions that require:
- Evaluating and selecting "best" evidence or answers
- Understanding paragraphs as a whole
- Identifying author's purpose or ideas

Students perform better on questions that:
- Ask about specific factual content ("according to")
- Focus on sentence-level or word-level understanding
- Require direct text lookup

### How to Run

1. Ensure Python 3 is installed (no external dependencies needed)
2. Place `quiz_questions.json` and `analysis.py` in the same directory
3. Run: `python3 analysis.py`
4. Results are saved to:
   - `output.json` - Structured data
   - `output.csv` - Human-readable comparison table

### Output Format
The CSV shows a frequency comparison table with columns:
- Word
- Frequency in low-scoring questions (per 1000 words)
- Frequency in high-scoring questions (per 1000 words)
- Difference (positive = more common in low-scoring, negative = more common in high-scoring)
