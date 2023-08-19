////// ##########   first snowflake ################
import React, { useState } from "react";
//import "./App.css";
import Dialog from "./Dialog";

export const FirstTable = () => {
  const [showDialog, setShowDialog] = useState(false);
  const [inputValue, setInputValue] = useState("");
  const [GUID, setGUID] = useState("");

  const handleButtonClick = () => {
    setShowDialog(true);
  };

  const handleSave = (value: string) => {
    // Handle the input value in the parent component
    console.log("Saved:", value);
    setInputValue(value);
    let newGUID = uuidv4();
    console.log(newGUID);
    setGUID(newGUID);
    console.log(GUID);
    handleCloseDialog();
    window.location.href = `http://localhost:5173/channels/${newGUID}`;

    // setTimeout(() => {
    //   console.log(GUID);
    // }, 3000);
  };

  ///channels/<GUID>
  // const redirect = () => {
  //   let channelGUID = uuidv4();
  //   setGUID(channelGUID);
  //   console.log(GUID);
  //   //window.location.href = `http://localhost:5173/channels/${GUID}`;
  // };

  const handleCloseDialog = () => {
    setShowDialog(false);
  };

  function uuidv4() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
      /[xy]/g,
      function (c) {
        const r = (Math.random() * 16) | 0,
          v = c == "x" ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      }
    );
  }

  return (
    <React.Fragment>
      {showDialog && <Dialog onClose={handleCloseDialog} onSave={handleSave} />}
      <h1>Messsenger app</h1>
      <button onClick={handleButtonClick}>Create channel</button>
      <br />
      <br />
      <br />
      <br />
      <div className="firstTable">
        <table>
          <tr>
            <th>#</th>
            <th>Channel</th>
            <th>Number of Users</th>
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
        <p>Input value from dialog: {inputValue}</p>
      </div>
    </React.Fragment>
  );
};
