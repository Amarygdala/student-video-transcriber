from django.shortcuts import render
from .models import Video
from .forms import VideoForm

import argparse
import io

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('api-key.json')


def transcribe_file_with_word_time_offsets(request):
    """Transcribe the given audio file synchronously and output the word time
    offsets."""
    print("Start")

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    print("checking credentials")

    client = speech.SpeechClient(credentials=credentials)

    print("Checked")
    with io.open('media/videos/mono.flac', 'rb') as audio_file:
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

    for result in response.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))

    return render(request, './studentvt/index.html', {
            'form': VideoForm(),
            'video': Video.objects.filter().order_by('-id')[0]

        })


def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            videofile = Video.objects.filter().order_by('-id')[0]
            return render(request, './studentvt/index.html', {
                'form': VideoForm(),
                'video': videofile

            })
    else:
        form = VideoForm()
        return render(request, './studentvt/index.html', {
            'form': form
        })
