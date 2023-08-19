import React, { useState } from "react";
import "./index.css";
//import { useNavigate } from "react-router-dom";

export const Create = () => {
  //const navigate = useNavigate();
  const [teacher1, setTeacher1] = useState("name1");
  const [teacher2, setTeacher2] = useState("name2");
  const [teacher3, setTeacher3] = useState("name3");

  //   const [teacher1GUID, setTeacher1GUID] = useState("");
  //   const [teacher2GUID, setTeacher2GUID] = useState("");
  //   const [teacher3GUID, setTeacher3GUID] = useState("");

  const [title, setTitle] = useState("title");
  //   const [titleGUID, setTitleGUID] = useState("");

  const [error, setError] = useState("");

  const handleSubmit = async (e: { preventDefault: () => void }) => {
    e.preventDefault();
    setError("");
    try {
      if (teacher1 === "" || teacher2 === "" || teacher3 === "" || title === "")
        throw "input must not be epmty";

      if (
        teacher1 === teacher2 ||
        teacher1 === teacher3 ||
        teacher3 === teacher2
      )
        throw "names must be unique";

      // block if everything was succsessful
      {
        let teacher1GUID = uuidv4();
        let teacher2GUID = uuidv4();
        let teacher3GUID = uuidv4();
        let titleGUID = uuidv4();
        const exami1 = { guid: teacher1GUID, name: teacher1 };
        const exami2 = { guid: teacher2GUID, name: teacher2 };
        const exami3 = { guid: teacher3GUID, name: teacher3 };
        let examiners = [exami1, exami2, exami3];
        const exam = {
          guid: titleGUID,
          title: title,
          examiners: examiners,
        };
        ///console.log(exam);
        // const name = "akdjvkasjv";
        // const altceva = "mmmm";
        // const post = {
        //   name: name,
        //   title: altceva,
        // };
        let id = 0;
        await fetch("http://localhost:3000/exams", {
          method: "POST",
          body: JSON.stringify(exam),
          headers: { "Content-Type": "application/json" },
        })
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
            id = data.id;
            console.log(id);
          });

        window.location.href = `http://localhost:5173/examination/dashboard/${titleGUID}/${id}`;
        return exam;
      }
    } catch (e) {
      setError(`you fucker: ${e}`);
    }
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
      <div className="create">
        <h2> Examination Creation Page</h2>
        <form onSubmit={handleSubmit}>
          <label>
            title:
            <input
              type="text"
              // required
              value={title}
              onChange={(e) => {
                setTitle(e.target.value);
              }}
            />
          </label>
          <br />
          <br />
          <label>
            first teacher:
            <input
              type="text"
              // required
              value={teacher1}
              onChange={(e) => setTeacher1(e.target.value)}
            />
          </label>
          <br />
          <br />

          <label>
            second teacher
            <input
              //required
              value={teacher2}
              onChange={(e) => setTeacher2(e.target.value)}
            ></input>
          </label>
          <br />
          <br />
          <label>
            third teacher:
            <input
              type="text"
              // required
              value={teacher3}
              onChange={(e) => setTeacher3(e.target.value)}
            />
          </label>
          <br />
          <br />

          <button>add exam</button>
        </form>
        {/* <p>{teacher1}</p>
        <p>{teacher2}</p>
        <p>{teacher3}</p> */}

        {error !== "" && <p>{error}</p>}
      </div>
    </React.Fragment>
  );
};
