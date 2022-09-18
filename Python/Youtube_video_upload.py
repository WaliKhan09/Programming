# Python code to upload video to your youtube channel.

# Importing required modules
from simple_youtube_api.Channel import Channel  #pip install simple_youtube_api
from simple_youtube_api.LocalVideo import LocalVideo    #pip install simple_youtube_api

# Loggin into channel
channel = Channel()
# Get these from your Google Consol
channel.login("client_secrets.json", "credentials.storage")

# Setting up the video that is going to be uploaded
video = LocalVideo(file_path="path_to_your_video")

# Setting snippets of video
video.set_title("Add title for your video") # Title
video.set_description("Add description for your video") # Description
video.set_tags(["tag_1", "tag_2", "tag_3"]) # Tags
video.set_category(27) # Category [Get category list here]
video.set_default_language("en-US") # Video Language
video.self_declared_made_for_kids = False # Made for kids or not

# Setting video status
video.set_embeddable(True)
video.set_license("creativeCommon") # License
video.set_privacy_status("public") # Video status (private/public)
video.set_public_stats_viewable(True)

# Setting thumbnail for video
video.set_thumbnail_path('path_to_thumbnail_of_your_video')

# Uploading video
video = channel.upload_video(video)

# Printing the results
print(video.id)

# Liking the video
video.like()
