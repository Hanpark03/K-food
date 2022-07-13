import React from 'react';

class SearchBar extends React.Component{		
	state:any;
	

	constructor(props:any) {
		super(props);				
		this.state = {
			"searchkeyword": "",
			"searchByKeyword": props["searchByKeyword"]
		};					
	}

	keywordOnChange = (e:any) => {		
		this.setState({
			"searchkeyword": e.target.value
		})
	}

	render() {
		return (
			<div>
				<div className="searchbar-div">
					<input
			          type="text"
			          className="searchbar-input"			          
			          onChange={(e) => this.keywordOnChange(e)}	
			          placeholder="  K-Food Search"
			        />
			        <img src="/icons/search_icon.png" className="searchbar-icon" onClick={ () => this.state.searchByKeyword(this.state.searchkeyword) }/>
				</div>
			</div>
		);
	}
}

export default SearchBar