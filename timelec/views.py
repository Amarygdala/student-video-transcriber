from django.shortcuts import render
from .models import Video
from .forms import VideoForm

import argparse
import io
import os

from pydub import AudioSegment
from google.oauth2 import service_account
from boto.s3.connection import S3Connection

credentials = service_account.Credentials.from_service_account_file('api-key.json')


def index(request):
    print("Start")

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    print("checking credentials")

    client = speech.SpeechClient(credentials=credentials)

    print("Checked")

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            videofile = Video.objects.filter().order_by('-id')[0]
            videopath = str(videofile.videofile)
            audio = AudioSegment.from_file("./media/" + videopath, "mp4")
            audio.export("./media/videos/" + str(videofile.name) + ".flac", format="flac")
            # convert audio to text here

            audio = AudioSegment.from_file("./media/videos/" + str(videofile.name), "flac")
            audio = audio.set_channels(1)
            audio.export("./media/videos/" + 'mono_' + str(videofile.name) + ".flac", format="flac")

            # convert audio to text here
            with io.open("./media/videos/" + 'mono_' + str(videofile.name) + ".flac", 'rb') as audio_file:
                content = audio_file.read()

            print("audio file read")

            audio = types.RecognitionAudio(content=content)

            print("config start")
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
                language_code='en-US',
                enable_word_time_offsets=True)

            print("Recognizing:")
            response = client.recognize(config, audio)
            print("Recognized")

            text = ""
            segment = ''
            for result in response.results:
                alternative = result.alternatives[0]
                segment = ('Transcript: {}'.format(alternative.transcript))

                for word_info in alternative.words:
                    word = word_info.word
                    start_time = word_info.start_time
                    segment += ('Word: {}, start_time: {}'.format(
                        word,
                        start_time.seconds + start_time.nanos * 1e-9))

                text += segment + "\n\n"
                segment = ''

            return render(request, './studentvt/index.html', {
                'form': VideoForm(),
                'video': videofile,
                'text': text,

            })
    else:
        form = VideoForm()
        return render(request, './studentvt/index.html', {
            'form': form
        })
