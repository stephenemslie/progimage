# ProgImage

A sample image processing api built on Django

## Running the server

With Docker:

```
docker-compose up -d
curl http://localhost:8000/images/
```

Then open `http://localhost:8000/` in your browser to browse the api.

## Endpoints

There is only one endpoint in the api: `/images/`. This is a restful resource, so the following can be done:

`curl -d @imagefile.jpg http://localhost:8000/images/`: upload an image
`curl http://localhost:8000/images/`: list all images
`curl http://localhost:8000/images/UUID/` get details about one image
`curl -X DELETE http://localhost:8000/images/UUID/` delete an image

