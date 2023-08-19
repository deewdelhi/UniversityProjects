import "./App.css";

import * as React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";

import { BookShowAll } from "./components/Books/BookShowAll";
import { BookDetails } from "./components/Books/BookDetail";
import { BookFilter } from "./components/Books/BookFilter";

import { PublishingHouseShowAll } from "./components/PublishingHouses/PublishingHouseShowAll";
import { PublishingHouseDetail } from "./components/PublishingHouses/PublishingHouseDetail";
import { PublishingHouseAdd } from "./components/PublishingHouses/PublishingHouseAdd";
import { PublishingHouseDelete } from "./components/PublishingHouses/PublishingHouseDelete";
import { PublishingHousesByNumberOfBooks } from "./components/PublishingHouses/PublishingHousesByNumberOfBooks";

// function App() {
//   const [count, setCount] = useState(0);

//   return (
//     <React.Fragment>
//       {/* <PublishingHouseShowAll /> */}

//       <div className="App"></div>
//     </React.Fragment>
//   );
// }
// export default App;

function App() {
  return (
    <React.Fragment>
      <Router>
        <AppMenu />

        <Routes>
          <Route
            path="/publishing-house"
            element={<PublishingHouseShowAll />}
          />
          <Route
            path="/publishing-house/:publishingHouseId/details"
            element={<PublishingHouseDetail />}
          />

          <Route path="/" element={<AppHome />} />

          <Route
            path="/publishing-house/add"
            element={<PublishingHouseAdd />}
          />
          <Route
            path="/publishing-house/:publishingHouseId/delete"
            element={<PublishingHouseDelete />}
          />
          <Route path="findbooks/" element={<BookFilter />} />

          <Route path="/book" element={<BookShowAll />} />
          <Route path="/book/:bookId/details" element={<BookDetails />} />

          <Route
            path="publishing-houses/count-smth/"
            element={<PublishingHousesByNumberOfBooks />}
          />

          {/* <Route path="/courses/:courseId/edit" element={<CourseDetails />} />
          <Route path="/courses/:courseId/delete" element={<CourseDelete />} />
          <Route path="/courses/add" element={<CourseAdd />} />
*/}
        </Routes>
      </Router>
    </React.Fragment>
  );
}

export default App;
