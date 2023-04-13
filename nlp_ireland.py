import datetime
import pandas as pd
import praw

reddit = praw.Reddit(client_id='Client_Id',
                        client_secret='client_secret',
                        user_agent='user_name')

query = 'Teaching Council AND Requirements'
country = "Ireland"

result = []

for post in reddit.subreddit("all").search(query, limit=500):
    for comment in post.comments:
        if isinstance(comment, praw.models.MoreComments):
            continue
        date = datetime.datetime.fromtimestamp(comment.created_utc)
        author_name = comment.author.name if comment.author else '[deleted]'
        result.append([query, post.url, post.title, comment.body, author_name, date.strftime("%Y-%m-%d"), country])

df = pd.DataFrame(result, columns=['Keyword', 'URL', 'Post_Title', 'Comment', 'Author_Name', 'Comment_Date', 'Country'])
# print(df)
# Save the dataframe to a CSV file
df.to_csv('nlp_ireland_ai9.csv', index=False)
print(df)
