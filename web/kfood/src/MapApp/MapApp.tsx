import React from 'react';
import mapboxgl from 'mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import SearchBar from './SearchBar'
import Icons from './Icons'
import SideArea from './SideArea'
import AccountPopup from './AccountPopup'
 
mapboxgl.accessToken = 'pk.eyJ1IjoieWltMDMzMSIsImEiOiJjbDU4b29xb2kwMXIzM2pvNmdpYWJsNDhyIn0.iQG6EUOyqCX6k6ON6gxQhA';

class MapApp extends React.Component{	
	state:any	
	
	constructor(props:any) {
		super(props);				
		this.state = {
			"lng": -87.62,
			"lat": 41.88,
			"zoom": 9,		
			"map": null,
			"sideProps": {
				"convertSideFlag": this.convertSideFlag,
				"getSideProps": this.getSideProps,
				"updateSideProps": this.updateSideProps,
				"selectFood": this.selectFood,
				"contentstype": 0 // 0 = nothing, 1 = category, 2 = menu, 3 = restaurant list, 4 = restaurant
			},
			"sideFlag": 0,
			"accountProps": {
				"convertAccountFlag": this.convertAccountFlag
			},
			"accountFlag": 0,
			"restaurantData": {}
		}	
		
		
		//Add Marker with Test Data
		this.state.restaurantData = {
		  "type": "FeatureCollection",
		  "features": [{
		      "type": "Feature",
		      "geometry": {
		        "type": "Point",
		        "coordinates": [-87.632440, 41.853040]
		      },
		      "properties": {
		        "title": "Ahjoomah's Apron",
		        "description": "Korean food in modern minimalist space",
		      }
		    },
		    {
		      "type": "Feature",
		      "geometry": {
		        "type": "Point",
		        "coordinates": [-87.681480, 41.957880]
		      },
		      "properties": {
		        "title": "Cho Sun Ok",
		        "description": "Traditional Korean fare & self-cook BBQ"
		      }
		    }
		  ]
		};
		this.state.categoryData = [
			{
				"title": "Category test",
				"foodData": [{
					"title": "Food test",
					"food": "Internal Food ID Test"
				}]
			}
		]
	}

	convertAccountFlag = (flag:number) => {
		this.setState({
			accountFlag : flag
		})		
	}

	convertSideFlag = (flag:number) => {
		this.setState({
			sideFlag : flag
		})		
	}

	updateSideProps = (sideFlag:any) => {
		this.setState({			
			sideProps : Object.assign({}, sideFlag),			
		})	
	}

	selectFood = (food:any) => {
		console.log("User selected food: " + food)
	}

	getSideProps = () => {
		return this.state.sideProps
	}

	markerOnClick = (restrauntData:any) => {
		let currentsideProps = Object.assign({}, this.state.sideProps)
		currentsideProps["restaurantData"] = restrauntData
		currentsideProps["contentstype"] = 4
		this.setState({
			sideFlag : 1,
			sideProps : Object.assign({}, currentsideProps),
			
		})			
	}

	categoryOnClick = () => {
		let currentsideProps = Object.assign({}, this.state.sideProps)
		currentsideProps["categoryData"] = this.state.categoryData
		currentsideProps["contentstype"] = 1
		this.setState({
			sideFlag : 1,
			sideProps : Object.assign({}, currentsideProps),
			
		})
	}

	restaurantOnClick = () => {
		this.convertSideFlag(1)
	}

	accountOnClick = () => {
		this.convertAccountFlag(this.state.accountFlag > 0 ? 0 : 1)
	}

	searchByKeyword = (keyword:string) => {
		if(keyword.length > 0){
			console.log("Search:" + keyword)
			this.convertSideFlag(1)
		}
	}

	componentDidMount() {		
		const map = new mapboxgl.Map({
			container: "map-container",
			style: 'mapbox://styles/mapbox/streets-v11',
			center: [this.state.lng, this.state.lat],
			zoom: this.state.zoom,
			maxZoom: 20,
			minZoom: 2
		});
		this.state.map = map
		//Add Zoom Control		
		map.addControl(new mapboxgl.NavigationControl(), 'bottom-right');		
		for(let i = 0; i < this.state.restaurantData.features.length; i = i + 1){			
			let marker:any = this.state.restaurantData.features[i];	
			var el = document.createElement('div');
			el.className = 'marker';
			el.innerHTML = '<span><b>' + (i + 1) + '</b></span>'
			el.addEventListener('click', () => {
				this.markerOnClick(marker)
			});
			// make a marker for each feature and add it to the map
			new mapboxgl.Marker(el)
			.setLngLat(marker.geometry.coordinates)
			.setPopup(new mapboxgl.Popup({
				offset: 25
			}) // add popups
			.setHTML('<h3>' + marker.properties.title + '</h3><p>' + marker.properties.description + '</p>'))
			.addTo(map);
		}
	}


	render() {						
		return (
			<div>
				<div id="map-container" className="map-container" />	
				{this.state.sideFlag > 0 ? <SideArea {...{"sideProps": this.state.sideProps}}/> : ""}	
				{this.state.accountFlag > 0 ? <AccountPopup {...{"accountProps": this.state.accountProps}}/> : ""}	
				<SearchBar {...{"searchByKeyword":this.searchByKeyword}}/>	
				<Icons {...{"iconurl":"/icons/food_bank_icon.png", "top":"10px", "left":"520px", "onClick":this.categoryOnClick}} />
				<Icons {...{"iconurl":"/icons/table_restaurant_icon.png", "top":"10px", "left":"580px", "onClick":this.restaurantOnClick}}/>
				<Icons {...{"iconurl":"/icons/manage_accounts_icon.png", "top":"10px", "right":" 60px", "onClick":this.accountOnClick}}/>				
			</div>
		);
	}
}

export default MapApp