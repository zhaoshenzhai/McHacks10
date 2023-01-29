# McHacks10

Hey, our project is Subreddit vibes, so one of the main goals of our project is to allow users to get an overall 'vibe' of a certain subreddit based on how 'positive' it is. Just to demonstrate, I have this random post here

https://www.reddit.com/r/aww/comments/exng3g/bunnies_flop_over_when_they_feel_completely_safe/

How it does this is that it first scrapes the page for all the comments in the post, and then uses the nltk library (natural language toolkit) to generate sentiments for all the comments. The data is then processed and displayed via matplotlib, which is the graphs that you are seeing now.

Now that was just for one post, but we can actually use this to generate the sentiment, or the vibe, of an entire subreddit. We can do this, for example, with the McGill subreddit, and simultaneously compare it with the UofT subreddit. We can maybe use the results to see which group of students is happier. So how this works is that it fetches the top posts of all time in both subreddits, scrapes the comments, evaluates them using nltk, processes the data, and displays the results in matplotlib. So the graph should be popping up now... and apparently McGill students leave less positive comments and more negative comments.

So, anyways, this is more of a proof of concept to show how webscrapping can be integrated with a sentiment analysis AI (we could have certainly used Cohere insteaad of nltk) to create many interesting and practical applications. An example of a practical application one that does customer review analysis, and classifies them as either positive or negative.
