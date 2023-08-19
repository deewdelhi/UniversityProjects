import { useParams, Link } from "react-router-dom";
import "./index.css";
import { useState, useEffect } from "react";
import { Exam } from "./Exam";
import { Examiner } from "./Examiner";

export const EDP = () => {
  const { titleId } = useParams();
  const [exam, setExam] = useState<Exam>();
  //const [error, setError] = useState(null);
  const [examiners, setExaminers] = useState<Examiner[]>([]);

  useEffect(() => {
    const fetchExam = async () => {
      const response = await fetch("http://localhost:3000/exams/" + titleId);

      const exam = await response.json();
      setExam(exam);
      const examiners = exam["examiners"];
      setExaminers(examiners);
    };
    fetchExam();
    console.log(exam);
    console.log(" examiners", examiners);
  }, [titleId]);

  return (
    <div>
      {exam && (
        <div>
          <h1>dashboard for {exam?.title}</h1>
          <ol>
            {examiners.map((examiner) => (
              <div>
                <Link
                  to={`http://localhost:5173/examination/session/${exam["guid"]}/grading/${examiner["guid"]}`}
                >
                  <li key={examiner["guid"]}>
                    {examiner["guid"]} {examiner["name"]}
                  </li>
                </Link>
              </div>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
};
