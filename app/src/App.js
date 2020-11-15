import fire from './fire.svg';
import './App.css';

function App() {
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
