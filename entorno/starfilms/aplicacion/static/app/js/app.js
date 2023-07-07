const API_KEY = "a7921e34";

$("#formulario-busqueda").submit((event) => {
  event.preventDefault();
  let titulo = $("#titulo").val();
  $.get(
    `https://www.omdbapi.com/?apikey=${API_KEY}&s=${titulo}`,
    (data) => {
      if (data.Response === "True") {
        let peliculas = data.Search;
        let listaPeliculas = $("#lista-peliculas");
        listaPeliculas.empty();
        peliculas.forEach((pelicula) => {
          let titulo = pelicula.Title;
          let imagen = pelicula.Poster !== "N/A" ? pelicula.Poster : "https://via.placeholder.com/300x450.png?text=No+disponible";
          let item = `<li><h3>${titulo}</h3><img src="${imagen}" alt="${titulo}"></li>`;
          listaPeliculas.append(item);
        });
      } else {
        alert(data.Error);
      }
    }
  );
});




