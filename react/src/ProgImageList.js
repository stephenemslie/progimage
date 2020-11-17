import React from "react";

async function fetchImageList() {
  const response = await fetch(`/images/`);
  const data = await response.json();
  return data;
}

export default function ProgImageList(props) {
  const [images, setImages] = React.useState();
  React.useEffect(() => {
    fetchImageList().then(images => {
      setImages(images);
    });
  }, []);
  return (
    <ul>
      {images &&
        images.map(image => {
          return <li>{image.id}</li>;
        })}
    </ul>
  );
}
