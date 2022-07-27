import React from "react";
import axios from 'axios';
import './App.css'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class App extends React.Component {

 state = {
        isLoading: false
    }

 handleFile = (event) => {
    event.preventDefault();

    const fileToUpload = event.target.files[0];
    this.setState({
      fileToUpload: fileToUpload,
      isLoading: false
    });
  };

  handleSubmitData = (event) => {
    event.preventDefault();

    let formData = new FormData();
    formData.append("upload", this.state.fileToUpload);

    axios.post("https://fishbackend.herokuapp.com", formData)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });

    setTimeout(() => this.setState({
            isLoading: true
        }), 17000);
  };

  render() {
    return (
        <>
            <h1 className="App-header"> Fish app predicts fish weights based on their dimensions! </h1>
            <div className="My-div"></div>
            <img src="https://fishweight.s3.amazonaws.com/static/fish.jpg" alt="fish" className="App-logo"/>
            <div className="My-div"></div>
            <div className="App">
                <input
                    type="file"
                    accept=".csv"
                    onChange={this.handleFile}
                />
                <button onClick={this.handleSubmitData}>Sample</button>
            </div>
            <div className="App">
                {this.state.isLoading === false &&
                <h1> Please wait 10 to 20 seconds after click... </h1>
                }
                {this.state.isLoading === true &&
                <img src="https://fishweight.s3.amazonaws.com/data/plot.png" alt="new"/>
                }
            </div>
        </>
    );
  };
};
export default App;
