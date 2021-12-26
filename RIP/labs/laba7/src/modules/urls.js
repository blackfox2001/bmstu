class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    films() {
        return `${this.url}films/`
    }

    film(id) {
        return `${this.url}films/${id}/`
    }
}

export const urls = new Urls()