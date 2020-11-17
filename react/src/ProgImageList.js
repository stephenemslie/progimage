import React from "react";

async function fetchImageList() {
  const response = await fetch(`/images/`);
  const data = await response.json();
  return data;
}

export default function ProgImageList(props) {
  const [images, setImages] = React.useState([]);
  React.useEffect(() => {
    fetchImageList().then(images => {
      setImages(images);
    });
  }, []);
  return (
    <ul>
      {images.map(image => {
        return (
          <li>
            <a href={`http://localhost:8000${new URL(image.image).pathname}`}>
              {image.id}
            </a>
          </li>
        );
      })}
    </ul>
  );
}
