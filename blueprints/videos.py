from flask import Blueprint, redirect, url_for

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
    return  {
        'file': file_name,
        'url': url
    }