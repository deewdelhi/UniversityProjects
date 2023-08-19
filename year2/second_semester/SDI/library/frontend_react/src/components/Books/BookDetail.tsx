import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
//import { BACKEND_API_URL } from "../../constants";
import { Book } from "../../models/Book";
import { Author } from "../../models/Author";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { BACKEND_API_URL } from "../../constants";

export const BookDetails = () => {
  const { bookId } = useParams();
  const [book, setBook] = useState<Book>();
  const [authors, setAuthors] = useState<Author[]>([]);

  useEffect(() => {
    const fetchBook = async () => {
      const response = await fetch(`${BACKEND_API_URL}/book/${bookId}/`);

      const book = await response.json();

      console.log(book);
      setBook(book);
      const authors = book["authors"];
      setAuthors(authors);
    };
    fetchBook();
  }, [bookId]);

  return (
    <Container>
      <Card>
        <CardContent>
          <IconButton component={Link} sx={{ mr: 3 }} to={`/book`}>
            <ArrowBackIcon />
          </IconButton>{" "}
          <h1>Book Details</h1>
          <p>Book Title: {book?.title}</p>
          <p>Book Publishing House: {book?.publishing_house.name}</p>
          <p>Book Description: {book?.description}</p>
          <p>Book Releasing Year: {book?.releasing_year}</p>
          <p>Book authors:</p>
          <ul>
            {authors.map((author) => (
              <li key={author["id"]}>{author["id"]}</li>
            ))}
          </ul>
        </CardContent>
        <CardActions>
          <IconButton
            component={Link}
            sx={{ mr: 3 }}
            to={`/book/${bookId}/edit`}
          >
            <EditIcon />
          </IconButton>

          <IconButton
            component={Link}
            sx={{ mr: 3 }}
            to={`/book/${bookId}/delete`}
          >
            <DeleteForeverIcon sx={{ color: "red" }} />
          </IconButton>
        </CardActions>
      </Card>
    </Container>
  );
};
