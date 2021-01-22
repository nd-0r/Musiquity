import React from 'react'
import axios from 'axios'
import logo from './logo.svg';
import './App.css';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.onSubmit = this.props.callback.bind(this);
    this.state = {
      searchText: '',
    };
  }
  handleSearch = function (text) {
    this.setState({ searchText: text })
  }
  render() {
    return (
      <div className = 'searchArea'>
        <input
          placeholder = "Enter a link or search for a song or album"
          onChange = {
            (e) => this.handleSearch(e.target.value)
          }
        />
        <button className = 'submitButton'
          onClick = {
            () => this.props.callback(this.state.searchText)
          }>
          Search
        </button>
      </div>
    )
  }
}

class App extends React.Component {

  state = {
    results: []
  }

  submitSearch = (text) => {
    let base_url = 'https://musiquity.herokuapp.com/search/?q=';
    let url_to_submit = base_url + text;
    let newResults;
    axios
      .get(url_to_submit)
      .then(response => {
        newResults = JSON.parse(JSON.parse(
          response.data
        ));
      });
    this.setState({
      results: newResults
    });
    console.log(this.results)
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
      </div>
    );
  }
}

export default App;
