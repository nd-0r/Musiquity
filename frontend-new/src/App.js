import React from 'react'
import SearchBar from './SearchBar'
import SearchResults from './SearchResults'
import axios from 'axios'
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

  state = {
    services: [],
    results: []
  }

  submitSearch = (text) => {
    let base_url = 'https://musiquity.herokuapp.com/search/?q=';
    let url_to_submit = base_url + text;
    axios
      .get(url_to_submit)
      .then(response => {
        this.results = JSON.parse(
          response.data
        );;
      });
  }

  componentDidMount() {
    let url_to_submit = 'https://musiquity.herokuapp.com/services/';
    axios
      .get(url_to_submit)
      .then(response => {
        this.services = JSON.parse(
          response.data
        );
        console.log(this.services)
      });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        <SearchBar callback={this.submitSearch}/>
        </header>
        <div className="Search-results">
          
        </div>
      </div>
    );
  }
}

export default App;
