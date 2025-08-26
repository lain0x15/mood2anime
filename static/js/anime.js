var first_lock_getAnimesByFilters = false;
var second_lock_getAnimesByFilters = false;

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("loaderFullFill").style.display = "block";

  const range1 = document.querySelector('#tailmetr1');
  range1.addEventListener('input', handleInputRange1);
  range1.addEventListener('change', change1);
  const range2 = document.querySelector('#tailmetr2');
  range2.addEventListener('input', handleInputRange2);
  range2.addEventListener('change', change2);

  document.getElementById('filter_button').addEventListener('click', show_filters);
  document.getElementById('close_anime_filter').addEventListener('click', close_filters);
  document.getElementById('sort_button').addEventListener('click', show_sort);

  getAnimesByFilters();
});

function setUrlParams(array){
  var url = new URL(window.location.href);
  var search_params = url.searchParams;
  array.forEach(element => {
    search_params.set(element.name, element.value)
  });
  url.search = search_params.toString();
  window.history.replaceState(null, null, url.toString());
}

function change1 () {
  const value1 = event.target.parentNode.parentNode.style.getPropertyValue('--value-1');
  setUrlParams([
    {name:'page', value:1},
    {name:'date_release_from', value:value1}
  ]);
  getAnimesByFilters();
}

function change2 () {
  const value2 = event.target.parentNode.parentNode.style.getPropertyValue('--value-2');
  setUrlParams([
    {name:'page', value:1},
    {name:'date_release_to', value:value2}
  ]);
  getAnimesByFilters();
}

function handleInputRange1() {
  const value2 = event.target.parentNode.parentNode.style.getPropertyValue('--value-2');
  if (parseInt(event.target.value) >= parseInt(value2)) {
    event.target.value = value2
  }
  if (event.target.value === max_date_release) {
    event.target.style.zIndex = max_date_release;
  } else {
    event.target.style.zIndex = min_date_release;
  }
  event.target.parentNode.parentNode.style.setProperty('--value-1',event.target.value);
  event.target.nextElementSibling.value = event.target.value;
}

function handleInputRange2() {
  const value1 = event.target.parentNode.parentNode.style.getPropertyValue('--value-1');
  if (parseInt(event.target.value) <= parseInt(value1)) {
    event.target.value = value1;
  }
  if (event.target.value === min_date_release) {
    event.target.style.zIndex = max_date_release;
  } else {
    event.target.style.zIndex = min_date_release;
  }
  event.target.parentNode.parentNode.style.setProperty("--value-2",event.target.value);
  event.target.nextElementSibling.value = event.target.value;
}

function show_filters() {
  location.hash = '#anime_filters';
}

function close_filters() {
  location.hash = '';
}

function show_sort() {
  document.getElementById("dropdown_sort").classList.toggle("show");
}

function renderPager(currentPage, maxPages){
    var maxVisiblePages = 7;
    var pager = document.getElementById("pager");
    pager.innerHTML = '';
    var halfVisiblePages = Math.floor(maxVisiblePages/2);
    nextPagesCount = maxVisiblePages - halfVisiblePages - (maxPages - currentPage + 1)
    if (nextPagesCount > 0 && (maxPages - currentPage) >= 0){
        halfVisiblePages += nextPagesCount;
    }

    for (let i = currentPage - 1; i > 0 && halfVisiblePages > 0; i--) {
        pager.innerHTML = '<li><a class="pagerLink" onclick="changePage(' + i + ')">'+i+'</a></li>' + pager.innerHTML;
        halfVisiblePages--;
        maxVisiblePages--;
    }

    for (let i = currentPage; i <= maxPages && i < maxVisiblePages + currentPage ; i++) {
        if (i == currentPage ) {
            pager.innerHTML+='<li class="active"><a>'+i+'</a></li>';
        } else {
            pager.innerHTML+='<li><a class="pagerLink" onclick="changePage(' + i + ')">'+i+'</a></li>';
        }
    }
}

function changePage(page){
    setUrlParams([
        {name:'page',value:page}
    ]);
    window.scrollTo(0, 0);
    getAnimesByFilters();
}

function setCheckedValueOfRadioButtonGroup(name, value) {
  let radios = document.getElementsByName(name);
  for (let radio of radios) {
    if (radio.value === value) {
      radio.checked = true;
      break;
    }
  }
}

function setGenreFilter(element,idGenre) {
    let params = new URLSearchParams(document.location.search);
    let filter_genre = params.get("filter_genres");

    radio_value = document.querySelector('input[name="' + idGenre + '"]:checked').value;

    console.log(event.target.name);
    if (!event.target.name){
        if (radio_value == 2){radio_value=-1}
        radio_value++;
        setCheckedValueOfRadioButtonGroup("" + idGenre, "" + radio_value);
    }

    if (filter_genre != null && filter_genre!="") {
        filter_genre=filter_genre.split("-");
    } else {
        filter_genre = new Array();
    }

    filter_genre.push(radio_value + "_" + idGenre);
    regex = new RegExp(/^[12]_\d+$/);
    filter_genre = filter_genre.filter((item) => regex.test(item));

    regex = new RegExp("^[^"+radio_value+"]_"+idGenre+"$");
    filter_genre = filter_genre.filter((item) => !regex.test(item));

    setUrlParams([
        {name:'page', value:1},
        {name:'filter_genres',value:filter_genre.join('-')}
    ]);
    getAnimesByFilters();
}

function getAnimesByFilters (){
    if (first_lock_getAnimesByFilters && !second_lock_getAnimesByFilters) {
        second_lock_getAnimesByFilters = true;
        setTimeout(() => {
            second_lock_getAnimesByFilters = false;
            getAnimesByFilters();
        }, 300);
        return 0;
    } else if (second_lock_getAnimesByFilters) {
        return 0;
    }

    first_lock_getAnimesByFilters = true;
    document.getElementById('animeRows').classList.add("blur");
    let params = new URLSearchParams(document.location.search);
    $.ajax({
        url: "/api/anime/get",
        headers: { 'X-CSRFToken': csrftoken },
        method: 'post',
        dataType: 'html',
        data: {
            date_release_from: params.get("date_release_from"),
            date_release_to: params.get("date_release_to"),
            filter_genres: params.get("filter_genres"),
            limit: params.get("limit"),
            page: params.get("page"),
            order_by: params.get("order_by")
        },
        success: function(data){
            var animes = JSON.parse(data).animes;
            let newAnimeRows = document.getElementById('animeRows').cloneNode(true);
            newAnimeRows.classList.remove("blur");
            newAnimeRows.innerHTML = '';
            animes.forEach((anime) => {
                var animeRow = document.createElement("div");
                animeRow.classList.add("animeRow");

                animeRowImg = document.createElement("img");
                animeRowImg.src = anime.portraitImage;
                animeRowImg.classList.add("animeRowImg");
                animeRow.appendChild(animeRowImg);

                animeRowInfo = document.createElement("div");
                animeRowInfo.classList.add("animeRowInfo");
                animeRowName = document.createElement("div");
                animeRowName.classList.add("animeRowName");
                animeRowNameLink = document.createElement("a");
                animeRowNameLink.href="/animePage/" + anime.url_name;
                animeRowNameLink.appendChild(document.createTextNode(anime.name));
                animeRowName.appendChild(animeRowNameLink);
                animeRowInfo.appendChild(animeRowName);

                animeRowText = document.createElement("span");
                animeRowText.classList.add("animeRowText");
                var dateRelease = new Date(anime.releaseYear);
                animeGenres = ""
                if (anime.genre.length) {
                    animeGenres += " / ";
                    anime.genre.forEach((element, idx) => {
                        if (idx == 0){
                            animeGenres += element;
                        } else {
                            animeGenres += ", " + element.toLowerCase();
                        }
                    });
                }
                animeRowText.appendChild(document.createTextNode(dateRelease.getFullYear() + " / " + anime.kind + animeGenres));
                animeRowInfo.appendChild(document.createElement("br"));
                animeRowInfo.appendChild(animeRowText);

                if (anime.description) {
                    animeDescription = document.createElement("p");
                    animeDescription.classList.add("animeDescription");
                    animeDescription.appendChild(document.createTextNode(anime.description.slice(0, 150) + "..."));
                    animeRowInfo.appendChild(animeDescription);
                }


                animeRow.appendChild(animeRowInfo);
                newAnimeRows.appendChild(animeRow);
            });
            if (animes.length == 0) {
                document.getElementById("not_found_anime").style.display = "block";
            } else {
                document.getElementById("not_found_anime").style.display = "none";
            }
            let oldNode = document.getElementById('animeRows');
            setTimeout(() => {
                oldNode.parentElement.replaceChild(newAnimeRows, oldNode);
                renderPager(JSON.parse(data).page, JSON.parse(data).pages);
                first_lock_getAnimesByFilters = false;
             }, 300);
             setTimeout(() => {  document.getElementById("loaderFullFill").style.display = "none"; }, 300);
        },
        error: function(jqXHR, exception){
            first_lock_getAnimesByFilters = false;
            if (!second_lock_getAnimesByFilters){
                setTimeout(() => {
                    getAnimesByFilters();
                }, 500);
            }
        }
    });
}

function show_genres_filter() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function change_size_genre_filter() {
    var height_myDropdown = 300;
    var myElement = document.getElementById('myDropdown');
    var myElementDp = document.getElementById('dropdown_id');
    var bounding = myElement.getBoundingClientRect();
    var boundingDp = myElementDp.getBoundingClientRect();

    if (boundingDp.bottom + height_myDropdown <= window.innerHeight) {
        myElement.style.transform = "translate(0px," + 0 + "px)";
        myElement.style.maxHeight = "" + height_myDropdown + "px";
    } else {
        myElement.style.maxHeight = "" + boundingDp.top + "px";
        myElement.style.transform = "translate(0px," + boundingDp.bottom * -1 + "px)";
    }
}

function change_sort(element,order_by){
    setUrlParams([
        {name:'page',value: 1},
        {name:'order_by',value:order_by}
    ]);
    document.getElementById('sort_name').textContent=element.innerHTML;
    getAnimesByFilters();
}

window.addEventListener('resize', () => {
  change_size_genre_filter();
});

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn') && !event.target.matches('.dropNoClose')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
    change_size_genre_filter();

    if (!event.target.matches('#sort_button') && !event.target.matches('#sort_name')) {
        var openDropdown = document.getElementById("dropdown_sort");
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
}