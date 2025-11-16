## Quiz Question Analysis

This script analyzes quiz questions to identify which words appear more frequently in questions students struggle with vs. questions they answer correctly.

### Setup

Requirements: Python 3 (uses only standard library)

Run the analysis:
```bash
python3 analysis.py
```

This generates `output.csv` and `output.json` with word frequency comparisons.

### Approach

Questions are split into two groups based on percent_correct:
- Low-scoring: < 50% (harder questions)
- High-scoring: > 50% (easier questions)

The script calculates word frequency per 1000 words in each group to account for the different number of questions. Words appearing more often in one group vs. the other show up clearly in the difference column.

### Results

Looking at the output, some interesting patterns emerge:

Words like "paragraph", "select", and "best" show up more in harder questions. These tend to be questions asking students to evaluate or choose the "best" evidence, or analyze specific paragraphs.

Words like "sentence", "word", and "according" appear more in easier questions. These are often straightforward questions about word meanings or factual recall ("according to the article...").

It seems students do better with direct, factual questions but struggle more with questions requiring evaluation and selection of evidence.

