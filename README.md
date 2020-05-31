# student-video-transcriber
## Inspiration
Teachers and students are having a hard time adjusting to an unfamiliar learning environment during the quarantine, unable to use the current applications like zoom to its fullest. After discussing what was wrong with the lectures, we decided that they were boring, unorganized, and hard to follow.

In order to help the students through COVID-19, we needed to make it so lectures are easier to pick apart and make the important information easier to access.

## What it does
Timelec takes a video that you provide and automatically transcribes the audio using Google Cloud Speech API so that you won't need to spend hours finding a particular topic the teacher talks about. Once you find what you are looking for through the text, you can click on it to jump through that part of the video. We also added a search function where students can type in keywords in the video and allow them to find a topic even faster without having to look through the transcript every time.

## How I (we) built it
We used Django for the backend, PostgreSQL (Heroku) as the database, HTML, Javascript, CSS and bootstrap boilerplate for frontend. We used Heroku to deploy our app.

## How to use
Upload your video and wait for the file to process.
Navigate to results to see the transcript. On larger files you can use CTRL+F to search for key words.
Enter the associated timestamp in the search bar below the results
Hit GO and the video will jump to the specified time.
# CONSTRAINTS
Please use Firefox, the site doesn't have full functionality with Chrome.
Feel free to use your own video, but there are constraints to video length and size. Video have to be less than a minute, and smaller than 10 MB. -here is a sample video you can use to test lecture.mp4

## Challenges I (we) ran into
I accidentally posted my Google API key on Github which resulted in some guy mining cryptocurrency with my Compute Engine.

Deploying to Heroku (was new for us).

## Accomplishments that I'm proud of
Being able to navigate to specific times in the video.
Transcribing the video with Google Cloud Speech-to-Text.
Converting .mp4 to .wav to .flac to mono channel .flac.
## What I learned
File conversion with ffmpeg and python. A great master named Xiang learned Heroku. How to use Bootstrap along with HTML. The meaning of stress.

## What's next for Timelec
A cleaner UI/UX is a good start.
Support for browsers other than Firefox.
Support for video longer than a minute and greater than 10 MB.
Additional functionality, adding timestamps on the video, displaying video.
