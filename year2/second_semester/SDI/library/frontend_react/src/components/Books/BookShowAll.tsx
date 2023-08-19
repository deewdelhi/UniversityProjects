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
  IconButton,
  Tooltip,
  TextField,
} from "@mui/material";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Book } from "../../models/Book";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import { BACKEND_API_URL } from "../../constants";

export const BookShowAll = () => {
  const [loading, setLoading] = useState(false);
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    setLoading(true);
    fetch(`${BACKEND_API_URL}/book/`)
      .then((response) => response.json())
      .then((data) => {
        setBooks(data);
        setLoading(false);
      });
  }, []);

  return (
    <Container>
      <h1>All books</h1>

      {loading && <CircularProgress />}

      {!loading && (
        // <IconButton component={Link} sx={{ mr: 3 }} to={`/book/add`}>
        //   <Tooltip title="Add a new book" arrow>
        //     <AddIcon color="primary" />
        //   </Tooltip>
        // </IconButton>
        // <IconButton component={Link} sx={{ mr: 3 }} to={`/findbook/`}>
        //   <Tooltip title="Filter" arrow>
        //     <AddIcon color="primary" />
        //   </Tooltip>
        // </IconButton>
        <TextField
          id="filter"
          label="Filter"
          variant="outlined"
          fullWidth
          sx={{ mb: 2 }}
        />
      )}
      {/* // ) && (
          //   <IconButton component={Link} sx={{ mr: 3 }} to={`/findbook/`}>
          //     <Tooltip title="Filter" arrow>
          //       <AddIcon color="primary" />
          //     </Tooltip>
          //   </IconButton>
          //   // onChange={(event) =>
          //   //   setCourse({ ...course, description: event.target.value })
          //   // }
          // )} */}
      {!loading && books.length > 0 && (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell align="right">Title</TableCell>
                <TableCell align="right">Publishing house</TableCell>
                <TableCell align="right">Description</TableCell>
                <TableCell align="center">Releasing year</TableCell>
                <TableCell align="center">Operations</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {books.map((book, index) => (
                <TableRow key={book.id}>
                  <TableCell component="th" scope="row">
                    {index + 1}
                  </TableCell>
                  <TableCell component="th" scope="row">
                    <Link
                      to={`/book/${book.id}/details`}
                      title="View book details"
                    >
                      {book.title}
                    </Link>
                  </TableCell>
                  <TableCell align="right">
                    {book.publishing_house?.name}
                  </TableCell>
                  <TableCell align="right">
                    {book.publishing_house.name}
                  </TableCell>
                  <TableCell align="right">{book.description}</TableCell>
                  <TableCell align="right">{book.releasing_year}</TableCell>
                  <TableCell align="right">
                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/book/${book.id}/details`}
                    >
                      <Tooltip title="View book details" arrow>
                        <ReadMoreIcon color="primary" />
                      </Tooltip>
                    </IconButton>

                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/book/${book.id}/edit`}
                    >
                      <EditIcon />
                    </IconButton>

                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/book/${book.id}/delete`}
                    >
                      <DeleteForeverIcon sx={{ color: "red" }} />
                    </IconButton>
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
