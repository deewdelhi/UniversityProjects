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
} from "@mui/material";

import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { BACKEND_API_URL } from "../../constants";
import { PublishingHouse } from "../../models/PublishingHouse";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";

export const PublishingHouseShowAll = () => {
  const [loading, setLoading] = useState(false);
  const [publishingHouses, setPublishingHouses] = useState<PublishingHouse[]>(
    []
  );

  useEffect(() => {
    setLoading(true);
    fetch(`${BACKEND_API_URL}/publishing-house/`)
      .then((response) => response.json())
      .then((data) => {
        setPublishingHouses(data);

        setLoading(false);
      });
  }, []);

  return (
    <Container>
      <h1>All Publishing Houses</h1>

      {loading && <CircularProgress />}
      {!loading && publishingHouses.length === 0 && (
        <p>No publishing houses found</p>
      )}
      {!loading && (
        <IconButton
          component={Link}
          sx={{ mr: 3 }}
          to={`/publishing-house/add`}
        >
          <Tooltip title="Add a new publishing house" arrow>
            <AddIcon color="primary" />
          </Tooltip>
        </IconButton>
      )}

      {!loading && publishingHouses.length > 0 && (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell align="right">Name</TableCell>
                <TableCell align="right">Headquarters</TableCell>
                <TableCell align="right">Founding Year</TableCell>
                <TableCell align="center">Operations</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {publishingHouses.map((publishingHouse, index) => (
                <TableRow key={publishingHouse.id}>
                  <TableCell component="th" scope="row">
                    {index + 1}
                  </TableCell>

                  <TableCell component="th" scope="row">
                    <Link
                      to={`/publishing-house/${publishingHouse.id}/details`}
                      title="View publishing house details"
                    >
                      {publishingHouse.name}
                    </Link>
                  </TableCell>

                  <TableCell align="right">
                    {publishingHouse.headquarters}
                  </TableCell>
                  <TableCell align="right">
                    {publishingHouse.founding_year}
                  </TableCell>
                  {/* <TableCell align="right">{publishingHouse.teacher?.name}</TableCell> */}
                  <TableCell align="right">
                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/publishing-house/${publishingHouse.id}/details`}
                    >
                      <Tooltip title="View publishing house details" arrow>
                        <ReadMoreIcon color="primary" />
                      </Tooltip>
                    </IconButton>

                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/publishing-house/${publishingHouse.id}/edit`}
                    >
                      <EditIcon />
                    </IconButton>

                    <IconButton
                      component={Link}
                      sx={{ mr: 3 }}
                      to={`/publishing-house/${publishingHouse.id}/delete`}
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
