import React from "react";

import "./AddTrailMap.css";

const AddTrailMap = props => {
  //   const [marker, setMarker] = useState([]);
  //   const [latLng, setLatLan] = useState([]);

  return (
    <>
      <div className="container-directions">
        <iframe
          width="100%"
          height="500"
          frameBorder="100px"
          style={{ border: "100px" }}
          referrerPolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyDg3BfPVTnY_CMZONz6wS4C0Y9jxlfShcU&&origin=LosAngeles+California
      &destination=Ridgecrest+Californias
        &zoom=4
        &maptype=satellite"
          allowFullScreen
          getposition="true"
          title="map-directions"
          marker="getPosition"
        ></iframe>
      </div>
      ;
    </>
  );
};

export default AddTrailMap;
