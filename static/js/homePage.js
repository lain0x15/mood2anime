document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("loaderFullFill").style.display = "block";

  getIDsAnime().then(function(result){
    animeIDs = result.sort(() => Math.random() - 0.5);
    animeIDsOffset = Math.floor(Math.random() * animeIDs.length);
    getAnimeByID(animeIDs[animeIDsOffset]);
  });
});

async function getIDsAnime() {
  const data = new URLSearchParams();
  const response = await fetch('/getIDsAnime', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-CSRFToken': csrftoken
    },
    body: data
  });
  const json = await response.json();
  return json.animeIDs;
}

function show_screenshot (offset){
  screenshot_offset += offset;
  var slides = document.getElementsByClassName("anime_image");
  if (0 > screenshot_offset){
    screenshot_offset = slides.length - 1;
  } else if (slides.length <= screenshot_offset) {
    screenshot_offset = 0;
  }
  var active_slides = document.getElementsByClassName("anime_image_active");
  Array.from(active_slides).forEach((element) => {
    element.classList.remove("anime_image_active");
  });
  slides[screenshot_offset].classList.add("anime_image_active");
}

function getAnimeByID (id){
    $.ajax({
        url: "/getAnimeByID/" + id,
        headers: { 'X-CSRFToken': csrftoken },
        method: 'post',
        dataType: 'html',
        data: {},
        success: function(data){
            var anime = JSON.parse(data).anime;
            old_innerContent = document.getElementById("innerContent");

            innerContent = document.createElement('div');
            innerContent.setAttribute('id', 'innerContent');

            anime_screenshots = document.createElement("div");
            anime_screenshots.setAttribute('id', 'anime_screenshots');

            anime_title = document.createElement("div");
            anime_title.setAttribute('id', 'anime_title');

            anime_info = document.createElement("div");
            anime_info.setAttribute('id', 'anime_info');

            anime_genres = document.createElement("div");
            anime_genres.setAttribute('id', 'anime_genres');

            anime_description = document.createElement("div");
            anime_description.setAttribute('id', 'anime_description');

            anime_buttons = document.createElement("div");
            anime_buttons.setAttribute('id', 'anime_buttons');

            if(anime.screenshots[0]) {
                screenshot_offset = 0;
                anime.screenshots.forEach((screenshot, idx)=>{
                   screen = document.createElement("img");
                   screen.src=screenshot;
                   screen.classList.add("anime_image");
                   if (idx == 0) {
                       screen.classList.add("anime_image_active");
                   }
                   anime_screenshots.appendChild(screen);
                });
                button = document.createElement("a");
                button.classList.add("prev");
                button.onclick = (event) => {show_screenshot(-1);};
                button.textContent = "❮";
                anime_screenshots.appendChild(button);
                button = document.createElement("a");
                button.classList.add("next");
                button.onclick = (event) => {show_screenshot(1);};
                button.textContent = "❯";
                anime_screenshots.appendChild(button);
            }

            var url_mask = anime_page.replace(/0/, anime.url_name);
            link_to_anime = document.createElement("a");
            link_to_anime.href = url_mask;
            link_to_anime.classList.add("link_to_anime");
            link_to_anime.textContent = anime.name;
            anime_title.appendChild(link_to_anime);

            const releaseDate = new Date(anime.releaseYear);
            releaseYear = releaseDate.getFullYear ();

            anime_info_release = document.createElement("span");
            anime_info_release.textContent = "Релиз " + releaseYear + "г. ";

            anime_info_star = document.createElement("span");
            anime_info_star.textContent = "     ";
            anime_info_star.style = "background-image: url(" + star_url + ")";
            anime_info_star.classList.add("scoreStar");

            anime_info_score = document.createElement("span");
            anime_info_score.textContent = " " + anime.review + "/10";

            anime_info.appendChild(anime_info_release);
            anime_info.appendChild(anime_info_star);
            anime_info.appendChild(anime_info_score);

            anime.genre.forEach((element) => {
                genre = document.createElement("div");
                genre.classList.add("genre");
                contentGenre = document.createElement("div");
                contentGenre.classList.add("contentGenre");
                contentGenre.textContent = element;
                genre.appendChild(contentGenre);
                anime_genres.appendChild(genre);
            });

            anime_description.textContent = anime.description;

            anime_buttons_bottoms = document.createElement("div");
            anime_buttons_bottoms.setAttribute('id', 'bottoms');

            previousButton = document.createElement("div");
            previousButton.setAttribute('id', 'previousButton');
            previousButton.classList.add("buttons");
            previousButton.textContent = "Предыдущее";
            previousButton.onclick = (event) => {
                animeIDsOffset--;
                if (animeIDsOffset < 0){
                    animeIDsOffset = animeIDs.length - 1;
                }
                getAnimeByID(animeIDs[animeIDsOffset]);
            };

            nextButton = document.createElement("div");
            nextButton.setAttribute('id', 'nextButton');
            nextButton.classList.add("buttons");
            nextButton.textContent = "Следующее";
            nextButton.onclick = (event) => {
                animeIDsOffset++;
                if (animeIDsOffset >= animeIDs.length){
                    animeIDsOffset = 0;
                }
                getAnimeByID(animeIDs[animeIDsOffset]);
            };

            anime_buttons_bottoms.appendChild(previousButton);
            anime_buttons_bottoms.appendChild(nextButton);

            anime_buttons.appendChild(anime_buttons_bottoms);

            innerContent.appendChild(anime_screenshots);
            innerContent.appendChild(anime_title);
            innerContent.appendChild(anime_info);
            innerContent.appendChild(anime_genres);
            innerContent.appendChild(anime_description);
            innerContent.appendChild(anime_buttons);
            old_innerContent.parentElement.replaceChild(innerContent, old_innerContent);


            setTimeout(() => {  document.getElementById("loaderFullFill").style.display = "none"; }, 300);
        }
    });
}