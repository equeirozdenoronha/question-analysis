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

    low_formatted = [{'word': item[0], 'count': item[1]} for item in low_f.most_common(10)]
    high_formatted = [{'word': item[0], 'count': item[1]} for item in high_f.most_common(10)]

    return low_formatted, high_formatted



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

def create_output(most_common_words, most_common_phrases):
    with open('output.json', 'w') as file:
        json.dump({
            'most_common_low_percentage_words': most_common_words[0],
            'most_common_high_percentage_words': most_common_words[1],
            'most_common_low_percentage_phrases': most_common_phrases[0],
            'most_common_high_percentage_phrases': most_common_phrases[1]
        }, file)
def create_output_csv(most_common_words, most_common_phrases):
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        
        # Write words grouped by performance
        writer.writerow(['Most Common Words in Low Scoring Questions'])
        writer.writerow(['Word', 'Number of Occurrences'])
        for word in most_common_words[0]:
            writer.writerow([word['word'], word['count']])
        writer.writerow([])

        writer.writerow(['Most Common Words in High Scoring Questions'])
        writer.writerow(['Word', 'Number of Occurrences'])
        for word in most_common_words[1]:
            writer.writerow([word['word'], word['count']])
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
    most_common_words, most_common_phrases = analyze_data()
    create_output(most_common_words, most_common_phrases)
    create_output_csv(most_common_words, most_common_phrases)

if __name__ == '__main__':
    main()