import React, { useEffect, useState } from "react";
import "./index.css";
import "./App.css";
import { Exam } from "./Exam";
//import { Examiner } from "./Examiner";
import { Link } from "react-router-dom";

export const FirstTable = () => {
  const [exams, setExams] = useState<Exam[]>([]);
  //const [error, setError] = useState(null);
  //const [examiners, setExaminers] = useState<Examiner[]>([]);

  useEffect(() => {
    const fetchExams = async () => {
      const response = await fetch("http://localhost:3000/exams/");

      const exam = await response.json();
      setExams(exam);
      //const examiners = exam["examiners"];
      //setExaminers(examiners);
    };
    fetchExams();
    console.log(exams);
    //console.log(examiners);
    //   .then((res) => {

    //     return res.json();
    //   })
    //   .then((data) => {
    //     setExam(data);
    //     const examiners = exam["examiners"];

    //     setError(null);
    //   })
    //   .catch((err) => {
    //     if (err.name === "AbortError") console.log("fetchAborted");
    //     else console.log(error);
    //   });
  }, []);

  //////// ##########   first snowflake ################
  //   return (
  //     <React.Fragment>
  //       <h1>Grading app</h1>
  //       <a href="http://localhost:5173/examination/create">
  //         <button>Create examination</button>
  //       </a>
  //       <br />
  //       <br />
  //       <br />
  //       <br />
  //       <div className="firstTable">
  //         <table>
  //           <tr>
  //             <th>#</th>
  //             <th>Examination title</th>
  //             <th>Dashboard link</th>
  //             <th>Meanest examiner</th>
  //           </tr>
  //           <tr>
  //             <th> 1 </th>
  //             <td></td>
  //             <td></td>
  //             <td></td>
  //           </tr>
  //           <tr>
  //             <th> 2</th>
  //             <td></td>
  //             <td></td>
  //             <td></td>
  //           </tr>
  //         </table>
  //       </div>
  //     </React.Fragment>
  //   );

  //-------------------------------------------------------------------------------------------

  // ######################   5th snowflake ###################################3
  return (
    <React.Fragment>
      <h1>Grading app</h1>
      <a href="http://localhost:5173/examination/create">
        <button>Create examination</button>
      </a>
      <br />
      <br />
      <br />
      <br />
      {exams && (
        <div className="firstTable">
          <table>
            <tr>
              <th>#</th>
              <th>Examination title</th>
              <th>Dashboard link</th>
              <th>Meanest examiner</th>
            </tr>

            {exams.map((exam) => (
              <tr>
                <th> {exam["id"]} </th>

                <td> {exam["title"]}</td>

                <td>
                  <Link
                    to={`http://localhost:5173/examination/dashboard/${exam["guid"]}/${exam["id"]}`}
                  >
                    {exam["guid"]}
                  </Link>
                </td>

                <td></td>
              </tr>
            ))}
          </table>
        </div>
      )}
    </React.Fragment>
  );
};
