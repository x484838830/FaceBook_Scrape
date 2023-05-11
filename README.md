# Facebook_Scraper /Facebook資料探勘/ Facebook數據獲取

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

## 重要程式說明
### 導入函數
        import pandas as pd
        from facebook_scraper import get_posts
        from time import sleep
        from random import randint
        import warnings


### 所要抓取的Facebook社群（以靠北住宿2.0為例）
###### 主要看網址後面的最後一格，以以靠北住宿2.0網址為例：https://www.facebook.com/cowbihotel
###### 可以看出最後一項為"cowbihotel"，所以我們fanpage就設定為'cowbihotel'。
        fanpage = 'cowbihotel'
       

### 所要抓取的項目
        P = pd.DataFrame(columns=['user_id', 'username', 'time', 'post_url', 'post_id', 'post_text', 'like_count', 'love_count', 'go_count', 'wow_count', 'haha_count', 'sad_count', 'angry_count', 'share_count', 'comment_count', 'comments'])

### 設定要抓取幾篇
        page_default = 200

### 抓取留言
        def comments_to_text(comments):
            if not comments:
                return ''
            comment_texts = []
            for comment in comments:
                commenter_name = comment['commenter_name']
                comment_text = comment['comment_text']
                comment_texts.append(f"{commenter_name}: {comment_text}")
            return '\n'.join(comment_texts)

### 設定要爬多少篇文章
###### 這裡以抓取200篇為例
        if i == 200:

### 爬完一篇要休息多久
###### 設定此項可以有效避免爬蟲
        sleep(randint(10, 60))


### 最後將結果存到Excel檔案內
    P.to_excel('facebook_data_200.xlsx', index=False) #存擋到Excel


## 最終成果展示
<img width="840" alt="螢幕擷取畫面 2023-05-11 234911" src="https://github.com/x484838830/FaceBook_Scrape/assets/71696727/ddc50698-38f5-49c3-8083-c697a8fd8713">

##### 希望此程式有幫助到你搜集所需的資料
##### 當然還有很多其他功能與Plugin，你也可以從官方文件中所查詢：https://github.com/kevinzg/facebook-scraper#post-example%E3%80%82
