import React from 'react';



class SideArea extends React.Component{		
	state:any
	constructor(props:any) {
		super(props);		
		this.state = {
			"sideProps": props["sideProps"]
		}
	}

	render() {
		return (
			<div className="side-div">
				<div className="backicon icon-div" onClick={() => this.state.sideProps.convertSideFlag(0)}>					
			        <img src="/icons/close_icon.png" className="general-icon"/>
				</div>
			</div>
		);
	}
}

export default SideArea