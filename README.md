# ProgImage

A sample image processing api built on Django

## Running the tests

With Docker:

```
docker-compose run --rm django test
```

## Running the server

With Docker:

```
docker-compose up
```

Then open http://localhost:8000/ in your browser to browse the api.

## Endpoints

There is only one endpoint in the api: `/images/`. This is a restful resource, so the following can be done:

#### upload an image
`curl -d @imagefile.jpg http://localhost:8000/images/`

#### list all images
`curl http://localhost:8000/images/`

#### get details about a single image
`curl http://localhost:8000/images/UUID/`

#### delete an image
`curl -X DELETE http://localhost:8000/images/UUID/`

#### rotate an image
`curl -d degrees=90 http://localhost:8000/images/UUID/rotate/`
