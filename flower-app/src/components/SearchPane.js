import React, { useState } from "react";
import { Box, Button, Container, Grid, Stack, Typography } from "@mui/material";
import WebCam from "react-webcam";
import Guess from "./Guess";
import axios from "axios";

function SearchPane() {
  const [pred, setPred] = useState([]);
  const videoConstraints = {
    width: 200,
    height: 200,
    facingMode: "environment",
  };

  const webcamRef = React.useRef(null);
  const capture = React.useCallback(() => {
    const imgSrc = webcamRef.current.getScreenshot();
    axios
      .post("/flower", { img: imgSrc })
      .then((response) => setPred(response.data.predictions))
      .catch((err) => console.log(err));
  }, [webcamRef]);

  //   const data = [
  //     { prob: 10.2, name: "sadfsafsafsfasdf" },
  //     { prob: 20.2, name: "xcv" },
  //   ];
  return (
    <div>
      <Container style={{ backgroundColor: "#222222" }}>
        <Typography style={{ fontSize: "50px", color: "white" }}>
          Flower Search
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <Stack justifyContent={"center"}>
              <WebCam
                style={{ width: "100%" }}
                audio={false}
                height={400}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={"100%"}
                videoConstraints={videoConstraints}
              ></WebCam>
              <Button onClick={capture}>Capture</Button>
            </Stack>
          </Grid>
          <Grid xs={6}>
            <Guess data={pred}></Guess>
          </Grid>
        </Grid>
      </Container>
    </div>
  );
}

export default SearchPane;
