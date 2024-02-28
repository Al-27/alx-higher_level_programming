$.ajax({url:"https://swapi-api.alx-tools.com/api/films/?format=json"}).done((obj)=>{
    for(let mov of obj.results )
        $("UL#list_movies").append(`<li>${mov.title}</li>`);
});