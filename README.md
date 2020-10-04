# YouTube Commenter Bot
This is a simple Python script to comment on videos chosen by keywords.
Please use the program in a fair way and do not abuse the API. Remember to follow the [YouTube API TOS](https://developers.google.com/youtube/terms/api-services-terms-of-service).

## Installation

1. `git clone https://github.com/WastefulNick/YouTube-Commenter.git`
2. `cd YouTube-Commenter`
3. `pip3 install -r requirements.txt`
4. Create a project at the [Google Developers Console](https://console.developers.google.com/)
5. Add the YouTube Data API v3 to the project
6. Create OAUTH credentials and either download the client_secret.json or fill in the one in the YouTube-Commenter folder
7. Fill in all the files in data/ 

	keywords.txt contains the keywords the bot will use to find videos

	prefixes.txt contains the first half of comments

	comments.txt contains the second half of comments
	
	The program combines prefixes.txt and comments.txt when commenting, this is an anti spam measure.
	
## Example

In the keywords.txt file there could for example be these keywords:
``` 
gaming
fun
random
```
the bot will then search up these terms, and collect the first resulting videos.



Now if the file prefixes.txt for example contains 
```
Hey, how's your day!
I just wanted to tell you: 
```
and the file comments.txt for example contains
```
Check out this video: youtube.com/watch?v=aaaaaaa
Keep up the good work man!
```

The program will then choose a random prefix, and combine it with the "body" comment:
```
I just wanted to tell you:

Check out this video: youtube.com/watch?v=aaaaaaa
```

This is the result which is commented on one of the videos, the comments change every time it comments (depending on the amount of prefixes/comments)