$.ajax({url:"https://swapi-api.alx-tools.com/api/people/5/?format=json"}).done((obj)=>{
    $("DIV#character").text(obj.name);
});