import React from 'react';



class AccountPopup extends React.Component{		
	state:any
	constructor(props:any) {
		super(props);		
		this.state = {
			"accountProps": props["accountProps"]
		}
	}

	render() {
		return (
			<div className="accountpopup-div">
				<a className="accountpopup-a">Profile</a>
			</div>
		);
	}
}

export default AccountPopup