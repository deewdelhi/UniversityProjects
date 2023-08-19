import { useParams } from "react-router-dom";
import "./index.css";
import React, { useEffect, useState } from "react";
import { Exam } from "./Exam";
//import { Examiner } from "./Examiner";

export const EGP = () => {
  const { titleGUID, examinerGUID } = useParams();
  const [exams, setExams] = useState<Exam[]>([]);
  //const [examiners, setExaminers] = useState<Examiner[]>([]);
  const [error, setError] = useState("");
  const [examinerName, setExaminerName] = useState("");
  const [isPending, setIsPending] = useState(true);
  //const [isValidate, setValidate] = useState(false);

  useEffect(() => {
    const fetchExams = async () => {
      //setIsPending(true);
      const response = await fetch("http://localhost:3000/exams/");
      const exam = await response.json();
      setExams(exam);
      console.log(exams);
    };
    fetchExams();

    validate();
  }, []);

  const validate = () => {
    setError("");
    let foundGUID = 0;
    if (exams) {
      exams.forEach((exam) => {
        const examinersnew = exam["examiners"];
        //setExaminers((prevExaminers) => [...prevExaminers, ...examinersnew]);
        if (exam["guid"] === titleGUID) foundGUID++;

        examinersnew.forEach((examiner) => {
          if (examiner["guid"] === examinerGUID) {
            foundGUID++;
            setExaminerName(examiner["name"]);
          }
        });
      });
    }
    console.log("kjshgjksk");
    if (foundGUID !== 2) setError("one or both guid are not valid");
    //setValidate(true);
    setIsPending(false);
    return "";
  };

  //------------------------------------------------------------

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
