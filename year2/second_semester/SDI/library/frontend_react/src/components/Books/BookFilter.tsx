import {
  TableContainer,
  Paper,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  CircularProgress,
  Container,
  Button,
} from "@mui/material";
import { BACKEND_API_URL } from "../../constants";

import { useEffect, useState } from "react";
import { Book } from "../../models/Book";
import { ChangeEvent } from "react";

export const BookFilter = () => {
  const [loading, setLoading] = useState(false);
  const [books, setBooks] = useState<Book[]>([]);
  const [inputText, setInputText] = useState("0 or sth");

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value);
  };

  useEffect(() => {
    setLoading(true);
    fetch(`${BACKEND_API_URL}/findbooks/`)
      .then((response) => response.json())
      .then((data) => {
        setBooks(data);

        setLoading(false);
      });
  }, []);

  const filter = () => {
    setLoading(true);
    fetch(`${BACKEND_API_URL}/findbooks/?value=` + inputText)
      .then((response) => response.json())
      .then((data) => {
        setBooks(data);
        setLoading(false);
      });
  };

  const sortBooks = () => {
    const sortedPlayers = [...books].sort((a: Book, b: Book) => {
      if (a.releasing_year < b.releasing_year) {
        return -1;
      }
      if (a.releasing_year > b.releasing_year) {
        return 1;
      }
      return 0;
    });
    console.log(sortedPlayers);
    setBooks(sortedPlayers);
  };

  return (
    <Container>
      <h1>Filtered Books</h1>
      <div>
        <Button sx={{ color: "white" }} onClick={sortBooks}>
          Sort books by year
        </Button>
        <Button sx={{ color: "white" }} onClick={filter}>
          Filter by year
        </Button>
        <input type="text" onChange={handleChange} value={inputText} />
      </div>

      {loading && <CircularProgress />}
      {!loading && books.length === 0 && <p>No books found</p>}
      {!loading}
      {!loading && books.length > 0 && (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell align="right">Title</TableCell>
                <TableCell align="right">Releasing year</TableCell>
                <TableCell align="right">PH</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {books.map((book, index) => (
                <TableRow key={book.id}>
                  <TableCell component="th" scope="row">
                    {index + 1}
                  </TableCell>

                  <TableCell component="th" scope="row">
                    {book.title}
                  </TableCell>

                  <TableCell align="right">{book.releasing_year}</TableCell>
                  <TableCell align="right">
                    {book.publishing_house["name"]}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Container>
  );
};
