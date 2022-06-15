import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import { Card, CardBody, CardTitle } from "reactstrap";
import "./HomePage.css";
import axios from "axios";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const [user, token] = useAuth();
  const [trails, setTrails] = useState([]);
  // const [cars, setCars] = useState([]);

  useEffect(() => {
    const fetchTrails = async () => {
      try {
        let response = await axios.get(
          "http://127.0.0.1:8000/api/trails/all/",
          {
            headers: {
              Authorization: "Bearer " + token,
            },
          }
        );
        setTrails(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchTrails();
  }, [token]);
  return (
    <div className="trail-container">
      <div>
        <h1 className="trail-header">{user.username}'s saved trails</h1>
      </div>
      <div className="trails-kept">
        {trails.map(trails => (
          <Card key={trails.id}>
            <CardTitle>{trails.trail_name}</CardTitle>
            <CardBody>
              <img
                alt="trail"
                src="https://picsum.photos/318/180"
                width="100%"
              />
            </CardBody>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default HomePage;

// useEffect(() => {
//   const fetchCars = async () => {
//     try {
//       let response = await axios.get("http://127.0.0.1:8000/api/cars/", {
//         headers: {
//           Authorization: "Bearer " + token,
//         },
//       });
//       setCars(response.data);
//     } catch (error) {
//       console.log(error.response.data);
//     }
//   };
//   fetchCars();
// }, [token]);
// return (
//   <div className="container">
//     <h1>Home Page for {user.username}!</h1>
//     {cars &&
//       cars.map(car => (
//         <p key={car.id}>
//           {car.year} {car.model} {car.make}
//         </p>
//       ))}
//   </div>
// );
