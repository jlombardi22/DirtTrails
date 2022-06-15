import { useState, useEffect } from "react";
import useAuth from "../../hooks/useAuth";
import axios from "axios";
import { Card, CardBody, CardTitle } from "reactstrap";
import "./Camp.css";

const Camp = props => {
  const [user, token] = useAuth([]);
  const [campsites, setCampsites] = useState([]);

  useEffect(() => {
    const fetchCamps = async () => {
      try {
        let response = await axios.get(
          "http://127.0.0.1:8000/api/campsites/all/",
          {
            headers: {
              Authorization: "Bearer " + token,
            },
          }
        );
        setCampsites(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchCamps();
  }, [token]);
  return (
    <div className="campsite-container">
      <div>
        <h1 className="campsite-header">{user.username}'s saved campsites</h1>
      </div>
      <div className="campsites-kept">
        {campsites.map(campsites => (
          <Card key={campsites.id}>
            <CardTitle>{campsites.campsite_name}</CardTitle>
            <CardBody>
              <img
                alt="campsite"
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

export default Camp;
