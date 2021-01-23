import React from 'react'

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