# Preview Container

Python web service to generate thumbnail images based on [Preview-generator](https://github.com/algoo/preview-generator) and [Flask](http://flask.pocoo.org/)

Build the image:

```bash
docker build -t preview-container .
```

## Run the web service

Assuming the documents are at `./documents` and you want to keep the cached thumbnail images in `./cache` you can run the container with

```bash
docker run --rm -d -v documents:/var/data -v cache:/var/preview-cache --name preview  -p 127.0.0.1:5000:5000 preview-container
```

You may verify the containers status via `localhost:5000/status`.

## Parameters for `/preview` (POST)

Returns a thumbnail image of the document as jpg.

#### path

- required: yes
- type: String
- description: path to the document in the filesystem

#### width

- required: no (default: height or 256)
- type: int
- description: width of the preview image

#### height

- required: no (default: width or 256)
- type: int
- description: height of the preview image

#### page

- required: no (default: -1)
- type: int
- description: number of the page that the thumbnail should be generated for (first page:0)

#### ignoreCache

- required: no (default: -1)
- type: boolean
- description: forced the fresh generation of a thumbnail even if it already exists in the cache

### example:

```json
{
  "path": "/var/data/example29.docx",
  "width": 100,
  "height": 150,
  "page": 80,
  "ignoreCache": true
}
```

## Parameters for `/pageNumbers` (POST)

Returns the total number of pages of the document.

#### path

- required: yes
- type: String
- description: path to the document in the filesystem

## Parameters for `/pageNumbers` (POST)

Returns the mime- type of the source document of the document.

#### path

- required: yes
- type: String
- description: path to the document in the filesystem

## TODO

- Exception handling
- Healthcheck
- Logging
