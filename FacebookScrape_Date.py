##此程式用來設定要爬幾篇臉書貼文
import pandas as pd
from facebook_scraper import get_posts
from time import sleep
from random import randint
import warnings


P = pd.DataFrame(columns=['user_id', 'username', 'time', 'post_url', 'post_id', 'post_text', 'like_count', 'love_count', 'go_count', 'wow_count', 'haha_count', 'sad_count', 'angry_count', 'share_count', 'comment_count', 'comments'])
fanpage = 'cowbihotel'  #https://www.facebook.com/taipei33，取網址後面的id
page_default = 200
i = 0

def comments_to_text(comments):
    if not comments:
        return ''
    comment_texts = []
    for comment in comments:
        commenter_name = comment['commenter_name']
        comment_text = comment['comment_text']
        comment_texts.append(f"{commenter_name}: {comment_text}")
    return '\n'.join(comment_texts)


for post in get_posts(fanpage, pages=page_default, cookies="www.facebook.com_cookies.txt", options={"reactors": True, "comments": True}):
    try:
        if i == 200:   ##此處用來設定要爬幾篇
            break

        new_row = pd.DataFrame({'user_id': [str(post['user_id'])],
                                'username': [str(post['username'])],
                                'time': [post['time']],
                                'post_url': [post['post_url']],
                                'post_id': [str(post['post_id'])],
                                'post_text': [post['post_text'].strip().replace("\n", "")] if post['post_text'] is not None else '',
                                'like_count': [post['reactions']['讚'] if post['reactions'] is not None and '讚' in post['reactions'].keys() else 0],
                                'love_count': [post['reactions']['大心'] if post['reactions'] is not None and '大心' in post['reactions'].keys() else 0],
                                'go_count': [post['reactions']['加油'] if post['reactions'] is not None and '加油' in post['reactions'].keys() else 0],
                                'wow_count': [post['reactions']['哇'] if post['reactions'] is not None and '哇' in post['reactions'].keys() else 0],
                                'haha_count': [post['reactions']['哈'] if post['reactions'] is not None and '哈' in post['reactions'].keys() else 0],
                                'sad_count': [post['reactions']['嗚'] if post['reactions'] is not None and '嗚' in post['reactions'].keys() else 0],
                                'angry_count': [post['reactions']['怒'] if post['reactions'] is not None and '怒' in post['reactions'].keys() else 0],
                                'share_count': [post['comments']],
                                'comment_count': [post['shares']],
                                'comments': [comments_to_text(post['comments_full'])]})

        P = pd.concat([P, new_row], ignore_index=True)

        warnings.filterwarnings("ignore")
        i = i + 1
        print("\n\t>>>>> DONE{}.....POST_ID: {}  {}\n\t>>>>> {}\n\n".format(i, str(post['post_id']), str(post['time']), str(post['post_url'])))
        sleep(randint(10, 60))

    except Exception as e:
        print(f"Error while processing post {i + 1}: {e}")
        continue


    P.to_excel('facebook_data_200.xlsx', index=False) #存擋到Excel
