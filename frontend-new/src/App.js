import React from 'react'
import logo from './logo.svg';
import './App.css';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.onSubmit = this.submitSearch.bind(this);
    this.state = {
      searchText: '',
    };
  }
  handleSearch = function (text) {
    this.setState({ searchText: text })
  }
  submitSearch = () => {
    console.log(this.state.searchText)
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
            () => this.submitSearch()
          }>
          Search
        </button>
      </div>
    )
  }
}

function App() {
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
      <SearchBar />
      </header>
    </div>
  );
}

export default App;
