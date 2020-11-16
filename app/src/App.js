import fire from './fire.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
// import { useInterval } from './useInterval';

function App() {
  const [data, setData] = useState({"ubuntu1": {"ip": ["112.116.44.3",51379],"information": {"location": "Building 3","description": "Reuse from pop bus project"},"seq": 0,"isFire": 1},"ubuntu2": {"ip": ["112.116.44.2",51379],"information": {"location": "Building 2","description": "fuck"},"seq": 0,"isFire": 1}});
  const [nodeList, setNodeList] = useState(Object.keys(data))
  
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
              <td>IP</td>
              <td>LOCATION</td>
              <td>DESCRIPTION</td>
              <td>STATUS</td>
            </tr>
          </div>
          <div className="tableBody">
          {
            nodeList.map((node)=>{
              return (<tr>
                <td>{node}</td>
                <td>{data[node].ip[0]}</td>
                <td>{data[node].information.location}</td>
                <td>{data[node].information.description}</td>
                <td>{data[node].isFire}</td>
            </tr>)
            })
          }
          </div>
          <div className="fire">
            <img src={fire} className="fire" alt="fire" />
          </div>

      </div>

    </div>
  );
}

export default App;
