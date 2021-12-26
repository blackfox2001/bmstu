const getObjects = async () =>{
    return await fetch('http://localhost:30000/Films/', {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []}
        })
}

export default getObjects
