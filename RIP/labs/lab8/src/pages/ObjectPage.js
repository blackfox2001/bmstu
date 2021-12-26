import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp.js";



function ObjectPage(params) {
    const FilmsList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>{FilmsList.NameFilms}</h2>
            <p>{FilmsList.FilmsAbout}</p>
            <Link to="/Films"><button>Назад</button></Link>
        </div>
    );
}

export default ObjectPage;
