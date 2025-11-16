from collections import Counter
import json
import csv
import re

# Analyze data: read the quiz dataset and process each question's text
# Separate questions into "low" and "high" groups based on percent_correct (< 0.5 and > 0.5)
# For both groups, gather words from question text (excluding stopwords), and count their frequency
# Format the lists of most common words for low and high groups
# In a similar way, gather the most common full-question phrases for both low and high groups
# Output the analysis results in JSON format to 'output.json', including both common words and phrases

stop={"the","a","an","and","or","but","to","of","in","on","for","with","is","are","was","were","be","by",
        "that","this","it","as","at","from","which","what","why","how"}

def analyze_data():
    with open('quiz_questions.json', 'r') as file:
        data = json.load(file)
        most_common_words = get_most_common_words(data)
        most_common_phrases = get_most_common_phrases(data)
        return most_common_words, most_common_phrases

def get_most_common_words(data):
    low=[]
    high=[]
    for q in data:
        text=q['text'].lower()
        words=re.findall(r"[a-z']+",text)
        if q['percent_correct']<0.5:
            low.extend(words)
        elif q['percent_correct']>0.5:
            high.extend(words)

    low_f=Counter([w for w in low if w not in stop])
    high_f=Counter([w for w in high if w not in stop])
    
    # Calculate totals for normalization
    total_low = len([w for w in low if w not in stop])
    total_high = len([w for w in high if w not in stop])
    
    # Get top words from both groups and combine
    all_words = set([w for w, c in low_f.most_common(20)] + [w for w, c in high_f.most_common(20)])
    
    word_comparison = []
    for word in all_words:
        low_count = low_f.get(word, 0)
        high_count = high_f.get(word, 0)
        low_freq = (low_count / total_low) * 1000
        high_freq = (high_count / total_high) * 1000
        
        word_comparison.append({
            'word': word,
            'low_count': low_count,
            'high_count': high_count,
            'low_freq': low_freq,
            'high_freq': high_freq
        })
    
    # Sort by difference to show most distinctive
    word_comparison.sort(key=lambda x: x['low_freq'] - x['high_freq'], reverse=True)
    
    return word_comparison



def get_most_common_phrases(data):
    low = [item for item in data if item['percent_correct'] < 0.5]
    high = [item for item in data if item['percent_correct'] > 0.5]
    
    most_common_low_words = [item.get('text') for item in low if item['text'] not in stop]
    most_common_high_words = [item.get('text') for item in high if item['text'] not in stop]
    low_f = Counter(most_common_low_words).most_common(10)
    high_f = Counter(most_common_high_words).most_common(10)

    low_formatted = [{'phrase': item[0], 'count': item[1]} for item in low_f]
    high_formatted = [{'phrase': item[0], 'count': item[1]} for item in high_f]
    return low_formatted, high_formatted

def create_output(word_comparison, most_common_phrases):
    with open('output.json', 'w') as file:
        json.dump({
            'word_frequency_comparison': word_comparison,
            'most_common_low_percentage_phrases': most_common_phrases[0],
            'most_common_high_percentage_phrases': most_common_phrases[1]
        }, file, indent=2)
def create_output_csv(word_comparison, most_common_phrases):
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        
        # Write word frequency comparison
        writer.writerow(['Word Frequency Comparison (per 1000 words)'])
        writer.writerow(['Word', 'Low-Scoring Freq', 'High-Scoring Freq', 'Difference'])
        for word in word_comparison:
            diff = word['low_freq'] - word['high_freq']
            writer.writerow([word['word'], f"{word['low_freq']:.2f}", 
                           f"{word['high_freq']:.2f}", f"{diff:+.2f}"])
        writer.writerow([])

        # Write phrases grouped by performance
        writer.writerow(['Most Common Phrases in Low Scoring Questions'])
        writer.writerow(['Phrase', 'Number of Occurrences'])
        for phrase in most_common_phrases[0]:
            writer.writerow([phrase['phrase'], phrase['count']])
        writer.writerow([])

        writer.writerow(['Most Common Phrases in High Scoring Questions'])
        writer.writerow(['Phrase', 'Number of Occurrences'])
        for phrase in most_common_phrases[1]:
            writer.writerow([phrase['phrase'], phrase['count']])
        writer.writerow([])


def main():
    word_comparison, most_common_phrases = analyze_data()
    create_output(word_comparison, most_common_phrases)
    create_output_csv(word_comparison, most_common_phrases)

if __name__ == '__main__':
    main()