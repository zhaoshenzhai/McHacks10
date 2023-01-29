import sys
import scrape

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def get_sentiments(sentences):
    """
    :param sentences: stores sentences
    :return: list [positive, neutral, negative]
    """

    sentiments = [0, 0, 0]
    cpds = []
    for s in sentences:
        sentiment = sia.polarity_scores(s)
        cpd = sentiment["compound"]
        cpds.append(cpd)

        if cpd > 0:
            index = 0
        elif cpd == 0:
            index = 1
        else:
            index = 2
        sentiments[index] += 1
    return sentiments, cpds

def get_percentage(sentiments):
    num_all = sentiments[0] + sentiments[1] + sentiments[2]
    if num_all == 0:
        return None
    pos_perc = round(sentiments[0] / num_all * 100, 2)
    neu_perc = round(sentiments[1] / num_all * 100, 2)
    neg_perc = round(sentiments[2] / num_all * 100, 2)
    # print("Positive: " + str(pos_perc) + "%\nNeutral: " + str(neu_perc) + "%\nNegative: " + str(neg_perc) + "%")
    return [pos_perc, neu_perc, neg_perc]

def vibe_per_post(url):
    sentences = scrape.get_sentences(url)
    sentiments, compounds = get_sentiments(sentences)
    result = get_percentage(sentiments)
    return result, compounds


def vibe_per_subreddit(url_list):
    pos_total = 0
    neu_total = 0
    neg_total = 0

    count = 0
    for url in url_list:
        sys.stdout.flush()
        sys.stdout.write("\r" + "Fetching vibes... " + str(count) + "/" + str(len(url_list)))
        vibe = vibe_per_post(url)[0]

        if vibe != None:
            pos_total = pos_total + vibe[0]
            neu_total = neu_total + vibe[1]
            neg_total = neg_total + vibe[2]
        count = count + 1

    print()
    return [pos_total, neu_total, neg_total]
