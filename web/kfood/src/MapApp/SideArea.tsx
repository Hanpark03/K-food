import React from 'react';



class SideArea extends React.Component{		
	state:any
	constructor(props:any) {
		super(props);		
		this.state = {
			"sideProps": props["sideProps"],
			"foodFlag": false
		}
	}

	onClickFood = (food:any) => {						
		this.state.sideProps.selectFood(food)
	}

	renderFood = (foodData:any) => {
		return(
			<div>				
				{foodData.map((data:any) => (
					<a onClick={() => this.onClickFood(data.food)} >{data.title}</a>
				))}
			</div>
		)
	}

	onClickCategory = (foodData:any) => {		
		let sideprops = this.state.sideProps.getSideProps()	
		sideprops["foodData"] = foodData
		sideprops["contentstype"] = 2
		this.state.sideProps.updateSideProps(sideprops)
	}

	renderCategory = (categoryData:any) => {
		return(
			<div>				
				{categoryData.map((data:any) => (
					<a onClick={() => this.onClickCategory(data.foodData)} >{data.title}</a>
				))}
			</div>
		)
	}

	onClickRestaurant = (restaurantData:any) => {
		this.state.sideProps.selectRestaurant(restaurantData)
	}

	renderRestaurantList = (restaurantList:any) => {
		return(
			<div>
				{restaurantList.features.map((data:any) => (
					<div>
						<a onClick={() => this.onClickRestaurant(data)} >{data.properties.title}</a>
						<br></br>
					</div>
				))}
			</div>
		)
	}

	renderRestaurant = (restaurantData:any) => {
		return(
			<div>
				{restaurantData.properties.title}
			</div>
		)
	}

	render() {
		let sideprops = this.state.sideProps.getSideProps()		
		
		return (
			<div className="side-div">
				<div className="backicon icon-div" onClick={() => this.state.sideProps.convertSideFlag(0)}>					
			        <img src="/icons/close_icon.png" className="general-icon"/>
				</div>
				<div className="side-contents">
					{sideprops.contentstype == 1 ? this.renderCategory(sideprops.categoryData) : ""}
					{sideprops.contentstype == 2 ? this.renderFood(sideprops.foodData) : ""}
					{sideprops.contentstype == 3 ? this.renderRestaurantList(sideprops.restaurantList) : ""}
					{sideprops.contentstype == 4 ? this.renderRestaurant(sideprops.restaurantData) : ""}
				</div>
				
			</div>
		);
	}
}

export default SideArea