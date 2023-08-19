import {
  Button,
  Card,
  CardActions,
  CardContent,
  IconButton,
  TextField,
} from "@mui/material";
import { Container } from "@mui/system";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { PublishingHouse } from "../../models/PublishingHouse";

import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
//import { Teacher } from "../../models/Teacher";

export const PublishingHouseAdd = () => {
  const navigate = useNavigate();

  const [PH, setPH] = useState<PublishingHouse>({
    name: "",
    headquarters: "",
    founding_year: 1, // TODO: also read the teacher_id from the form (NOT from the user!)
  });

  //const [teachers, setTeachers] = useState<Teacher[]>([]);

  //   const fetchSuggestions = async (query: string) => {
  //     try {
  //       const response = await axios.get<Teacher[]>(
  //         `${BACKEND_API_URL}/teachers/autocomplete?query=${query}`
  //       );
  //       const data = await response.data;
  //       setTeachers(data);
  //     } catch (error) {
  //       console.error("Error fetching suggestions:", error);
  //     }
  //   };

  //   const debouncedFetchSuggestions = useCallback(
  //     debounce(fetchSuggestions, 500),
  //     []
  //   );

  //   useEffect(() => {
  //     return () => {
  //       debouncedFetchSuggestions.cancel();
  //     };
  //   }, [debouncedFetchSuggestions]);

  const addPH = async (event: { preventDefault: () => void }) => {
    event.preventDefault();
    try {
      await axios.post(`${BACKEND_API_URL}/publishing-house/`, PH);
      navigate("/publishing_house");
    } catch (error) {
      console.log(error);
    }
  };

  //   const handleInputChange = (event: any, value: any, reason: any) => {
  //     console.log("input", value, reason);

  //     // if (reason === "input") {
  //     //   debouncedFetchSuggestions(value);
  //     // }
  //   };

  return (
    <Container>
      <Card>
        <CardContent>
          <IconButton component={Link} sx={{ mr: 3 }} to={`/publishing-house`}>
            <ArrowBackIcon />
          </IconButton>{" "}
          <form onSubmit={addPH}>
            <TextField
              id="name"
              label="Name"
              variant="outlined"
              fullWidth
              sx={{ mb: 2 }}
              onChange={(event) => setPH({ ...PH, name: event.target.value })}
            />
            <TextField
              id="headquarters"
              label="Headquarters"
              variant="outlined"
              fullWidth
              sx={{ mb: 2 }}
              onChange={(event) =>
                setPH({ ...PH, headquarters: event.target.value })
              }
            />
            <TextField
              id="founding_year"
              label="Founding Year"
              variant="outlined"
              fullWidth
              sx={{ mb: 2 }}
              onChange={(event) =>
                setPH({ ...PH, founding_year: +event.target.value })
              }
            />

            {/* <Autocomplete
                id="teacher_id"
                options={teachers}
                getOptionLabel={(option) => `${option.name} - ${option.email}`}
                renderInput={(params) => (
                  <TextField {...params} label="Teacher" variant="outlined" />
                )}
                filterOptions={(x) => x}
                onInputChange={handleInputChange}
                onChange={(event, value) => {
                  if (value) {
                    console.log(value);
                    setPH({ ...course, teacher_id: value.id });
                  }
                }}
              /> */}

            <Button type="submit">Add Publishing House</Button>
          </form>
        </CardContent>
        <CardActions></CardActions>
      </Card>
    </Container>
  );
};
