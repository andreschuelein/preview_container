from preview_generator.manager import PreviewManager
from flask import Flask, send_file, request, json
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"status": "up"}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/preview', methods=['POST'])
def get_jpeg_preview():

    jsonRequest = request.get_json()
    if 'path' not in jsonRequest:
        raise ValueError('path required')
    else:
        source_document = request.json['path']
        print('source_document: ', source_document)

    if 'width' not in jsonRequest and 'height' not in jsonRequest:
        width = height = 256
    else:
        if 'width' in jsonRequest and 'height' in jsonRequest:
            width = jsonRequest['width']
            height = jsonRequest['height']
        else:
            if 'width' in jsonRequest:
                width = height = jsonRequest['width']
            if 'height' in jsonRequest:
                width = height = jsonRequest['height']

    print('width: ', width)
    print('height: ', height)

    if 'page' not in jsonRequest:
        page = -1
    else:
        page = jsonRequest['page']
    print('page: ', page)

    if 'ignoreCache' not in jsonRequest:
        ignoreCache = False
    else:
        ignoreCache = jsonRequest['ignoreCache']
    print('ignoreCache: ', ignoreCache)

    cache_path = '/var/preview-cache'
    manager = PreviewManager('/var/preview-cache/', create_folder=True)
    preview_path = manager.get_jpeg_preview(
        source_document, height=height, width=width, force=ignoreCache, page=page)
    return send_file(preview_path, mimetype='image/jpg')


@app.route('/pageNumbers', methods=['POST'])
def get_page_nb():

    jsonRequest = request.json
    if 'path' not in jsonRequest:
        raise ValueError('path required')
    else:
        source_document = request.json['path']
        print('source_document: ', source_document)

    cache_path = '/var/preview-cache'
    manager = PreviewManager('/var/preview-cache/', create_folder=True)
    get_page_nb = manager.get_page_nb(source_document)

    response = app.response_class(
        response=json.dumps({"pages": get_page_nb}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/mimetype', methods=['POST'])
def get_mimetype():

    jsonRequest = request.json
    if 'path' not in jsonRequest:
        raise ValueError('path required')
    else:
        source_document = request.json['path']
        print('source_document: ', source_document)

    cache_path = '/var/preview-cache'
    manager = PreviewManager('/var/preview-cache/', create_folder=True)
    mimetype = manager.get_mimetype(source_document)

    response = app.response_class(
        response=json.dumps({"mimetype": mimetype}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")

    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
