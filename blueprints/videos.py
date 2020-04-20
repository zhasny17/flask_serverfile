from flask import Blueprint, redirect, url_for, g
import os

bp = Blueprint('video', __name__)

@bp.route('/videos/<string:video_id>', methods=['GET'])
def get_videos(video_id):
    file_name = f'{video_id}/master.m3u8'
    url = url_for(
        'static',
        _external=True,
        _scheme='http',
        filename=file_name
    )
    print('!!!!!! IP', os.environ['SERVER_NAME'])
    url = url.replace('127.0.0.1', '142.93.249.97')
    return  {
        'file': file_name,
        'url': url
    }