import { useState, useEffect } from "react";
	import { Link } from "react-router-dom";
	import HeaderComp from "../components/HeaderComp.js";
	import getObjects from "../modules/GetObjects.js";
	

	

	function ListPage() {
	

	    const [FilmsList, setFilmsList] = useState([])
	    const [FilmsNames, setFilmsNames] = useState([])
	

	    const handleObjectsList = async () => {
	        const Types = []
	        const Films = await getObjects()
	        for (let film of Films) {
	            Types.push(Films['NameFilm']);
	        }
	        setFilmsList(Films)
	        setFilmsNames(NameFilm)
	    }
	

	    useEffect(()=>{
	        handleObjectsList()
	    }, [])
	

	    return (
	        <div>
	            <ul>
	                {FilmName.map((NameFilm)=>{
	                    return (
	                        <li key={NameFilm}>
	                            <Link to={{pathname: "/Films/object", data: FilmsList.find(obj => obj.NameFilm == NameFilm)}}>{NameFilm}</Link>
	                        </li>
	                    )
	                })}
	            </ul>
	        </div>
	    );
	}
	

	export default ListPage;
