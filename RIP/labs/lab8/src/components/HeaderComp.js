import { Link } from "react-router-dom";

function HeaderComp() {
    return (
        <div>
            <Link to='/'>Главная страница</Link>
            <hr></hr>
            <p>Группа: РТ5-51Б</p>
            <p>Студентка: Стадник Елена Романовна</p>



        </div>
    );
}

export default HeaderComp;
