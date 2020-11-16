import fire from './fire.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import { useInterval } from './useInterval';

function App() {
  const [data, setData] = useState({"ubuntu1": {"ip": ["112.116.44.3",51379],"information": {"location": "Building 3","description": "Reuse from pop bus project"},"seq": 0,"isFire": 1},"ubuntu2": {"ip": ["112.116.44.2",51379],"information": {"location": "Building 2","description": "fuck"},"seq": 0,"isFire": 1}});

  // useInterval(async () => {
  //   // console.log("effect")
  //   fetch(
  //     `http://localhost:8000/poll`,
  //     {
  //       method: "GET",
  //     }
  //   )
  //     .then(res => res.json())
  //     .then(response => {
  //       console.log(response)
  //       setData(response)
  //     })
  //     .catch(error => console.log(error));
  // }, 1000);



  return (
    <div className="bg">
      <div className="header">
        FAI MAI
      </div>
      <div className="table">
          <div className="tableHeader">
            <tr>
              <td>NODE</td>
              <td>LOCATION</td>
              <td>STATUS</td>
            </tr>
          </div>

          <div className="tableBody">
            <tr>
              <td>A121212</td>
              <td>Engineer3</td>
              <td>normal</td>
            </tr>
            <tr>
              <td>B121412</td>
              <td>Engineer4</td>
              <td>normal</td>
            </tr>
            <tr className="disconnected">
              <td>C121212</td>
              <td>Engineer3</td>
              <td>disconnected</td>
            </tr>
          </div>
          <div className="fire">
            <img src={fire} className="fire" alt="fire" />
          </div>

      </div>

    </div>
  );
}

export default App;
