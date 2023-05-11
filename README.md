# Facebook爬蟲

##### 作者所使用Python軟件為Facebook-Scraper，可詳閱此官方文件：https://github.com/kevinzg/facebook-scraper#post-example。
##### 作者測試與更改之程式碼，皆為2023/05/01測試，測試python軟體為3.11，若後續需更新或任何問題在請聯繫。


## 安裝套件
##### 使用pypl方式安裝

    pip install facebook-scraper

##### 或是從官方文件安裝

    pip install git+https://github.com/kevinzg/facebook-scraper.git

## Cookie獲取
#### 在瀏覽器安裝Cookie.txt擴充套件: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
<img width="770" alt="image" src="https://github.com/x484838830/FaceBook_Scrape/assets/71696727/3de08da0-a834-49c2-9a11-6a8e9c03a73f">



## 實作範例說明:

### 首先獲取自己的Facebook的cookie
##### 進入到自己的Facebook頁面 (https://www.facebook.com/)
##### 接著Get cookies.txt LOCALLY擴充元件來獲取Cookie，按下Export
<img width="375" alt="image" src="https://github.com/x484838830/FaceBook_Scrape/assets/71696727/3d107b70-9a37-4345-a35b-f4934726d9f8">

##### 將獲取的cookies.txt放置在自己的資料夾內

### 程式說明
##### 導入函數
##### 此程式用來設定要爬幾篇臉書貼文
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
