from textblob import TextBlob

print("================================")
print("      SENTIMENT ANALYZER")
print("================================")

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

print("\nYour Text:")
print(text)

print("\nPolarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")