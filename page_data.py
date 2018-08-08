from __future__ import print_function
import facebook



page_access_token = 'your_page_access_token_here'

graph = facebook.GraphAPI(page_access_token, version="2.7")


post_comment = graph.get_object(id='396123467586066_396159340915812', fields='likes,comments')

comment_replies = graph.get_object(id='396159340915812_396178430913903',fields='comments')

post_comments = post_comment['comments']

post_likes = post_comment['likes']

replies = comment_replies['comments']

print("Likes of the people on this post:\n",post_likes['data'])

print("Post comments:\n",post_comments['data'])

print("Replies on the above comment:\n",replies['data'])

print()

post = graph.get_object(id='DopeLinesRappersWrote', fields='feed')

all_posts = post['feed']

all_posts_data = all_posts['data']

for each_data in (range(len(all_posts_data))):
    
    print('Displaying each post of this page Dope Lines Rappers Wrote till date :\n')
    
    print("Post "+str(each_data)+" data is "+str(all_posts_data[each_data]))
    
    print()
