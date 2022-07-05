import React from 'react';
import mapboxgl from 'mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
 
mapboxgl.accessToken = 'pk.eyJ1IjoieWltMDMzMSIsImEiOiJjbDU4b29xb2kwMXIzM2pvNmdpYWJsNDhyIn0.iQG6EUOyqCX6k6ON6gxQhA';

class MapApp extends React.Component{
	mapContainer: React.RefObject<HTMLDivElement>;	
	lng:number; 
	lat:number;
	zoom:number;

	constructor(props:any) {
		super(props);		
		this.lng = -87.62;
		this.lat = 41.88;
		this.zoom = 9;	
		this.mapContainer = React.createRef();
	}
	componentDidMount() {		
		const map = new mapboxgl.Map({
			container: this.mapContainer.current as HTMLElement,
			style: 'mapbox://styles/mapbox/streets-v11',
			center: [this.lng, this.lat],
			zoom: this.zoom
		});
	}


	render() {
		return (
			<div>
				<div ref={this.mapContainer} className="map-container" />
			</div>
		);
	}
}

export default MapApp