import React from 'react';



class Icons extends React.Component{	
	iconurl:string; 
	top:number;
	left:number;
	right:number;
	onClick: any;

	constructor(props:any) {
		super(props);		
		this.iconurl = props["iconurl"];		
		this.top = props["top"];
		this.left = props["left"];
		this.right = props["right"];
		this.onClick = props["onClick"]
	}

	render() {
		return (
			<div style={{"position":"fixed", "top":this.top, "left":this.left, "right":this.right }} onClick={ () => this.onClick(1)}>
				<div className="icon-div">					
			        <img src={this.iconurl} className="general-icon"/>
				</div>
			</div>
		);
	}
}

export default Icons