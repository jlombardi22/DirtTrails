import React from "react";
const Map = props => {
  return (
    <div className="container" id="map">
      <iframe
        width="100%"
        height="500"
        frameBorder="100px"
        style={{ border: "100px" }}
        referrerPolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps/embed/v1/view?key=AIzaSyDg3BfPVTnY_CMZONz6wS4C0Y9jxlfShcU&center=38.572551,-100.784119
        &zoom=4
        &maptype=satellite"
        allowFullScreen
      ></iframe>
    </div>
  );
};

export default Map;
