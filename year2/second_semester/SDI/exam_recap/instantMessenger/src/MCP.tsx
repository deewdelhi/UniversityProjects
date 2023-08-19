import { useParams } from "react-router-dom";
import "./index.css";
import React, { useEffect, useState } from "react";
import { Channel } from "./Channel";

export const MCP = () => {
  const { GUID } = useParams();
  const [error, setError] = useState("");
  const [isPending, setIsPending] = useState(true);
  const [userNickname, setUserNickName] = useState("");
  const [channels, setChannels] = useState<Channel[]>([]);

  useEffect(() => {
    const fetchChannels = async () => {
      const response = await fetch("http://localhost:3000/channels/");
      const channel = await response.json();
      setChannels(channel);
      console.log(channels);
    };
    fetchChannels();

    validate();
  }, []);

  const validate = () => {
    setError("");
    let foundGUID = 0;
    if (channels) {
      channels.forEach((channel) => {
        if (channel["guid"] === GUID) {
          foundGUID++;
          setUserNickName();
        }
      });
    }

    if (foundGUID !== 1) setError("guid is not valid");
    //setValidate(true);
    setIsPending(false);
    return "";
  };

  return (
    <React.Fragment>
      {!isPending && (
        <div>
          <button onClick={() => validate()}>validate</button>
          <div>{error !== "" && <p>{error}</p>}</div>
          <div>
            {error === "" && (
              <div>
                <h1>gradebook for examiner : {examinerName} </h1>
                <table>
                  <tr>
                    <th>#</th>
                    <th>Student Name</th>
                    <th>Grade</th>
                  </tr>
                  <tr>
                    <th> 1 </th>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr>
                    <th> 2</th>
                    <td></td>
                    <td></td>
                  </tr>
                </table>
              </div>
            )}
          </div>
        </div>
      )}
    </React.Fragment>
  );
};
