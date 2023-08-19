import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { PublishingHouse } from "../../models/PublishingHouse";
import { Book } from "../../models/Book";
//import { BookShowAll } from "../Books/BookShowAll";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const PublishingHouseDetail = () => {
  const { publishingHouseId } = useParams();
  const [PH, setPH] = useState<PublishingHouse>();
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    const fetchPH = async () => {
      // TODO: use axios instead of fetch
      // TODO: handle errors
      // TODO: handle loading state

      const response = await fetch(
        `${BACKEND_API_URL}/publishing-house/${publishingHouseId}/`
      );

      const PH = await response.json();
      console.log(PH);
      setPH(PH);
      const books = PH["books"];
      setBooks(books);
    };
    fetchPH();
  }, [publishingHouseId]);

  return (
    <Container>
      <Card>
        <CardContent>
          <IconButton component={Link} sx={{ mr: 3 }} to={`/publishing-house`}>
            <ArrowBackIcon />
          </IconButton>{" "}
          <h1>PH Details</h1>
          <p>PH Name: {PH?.name}</p>
          <p>PH Headquarters: {PH?.headquarters}</p>
          <p>PH Founding Year: {PH?.founding_year}</p>
          <p>PH Books:</p>
          <ul>
            {books.map((book) => (
              <li key={book["id"]}>{book["title"]}</li>
            ))}
          </ul>
        </CardContent>
        <CardActions>
          <IconButton
            component={Link}
            sx={{ mr: 3 }}
            to={`/publishing-house/${publishingHouseId}/edit`}
          >
            <EditIcon />
          </IconButton>

          <IconButton
            component={Link}
            sx={{ mr: 3 }}
            to={`/publishing-house/${publishingHouseId}/delete`}
          >
            <DeleteForeverIcon sx={{ color: "red" }} />
          </IconButton>
        </CardActions>
      </Card>
    </Container>
  );
};
