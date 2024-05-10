function setUrlParams(array){
    var url = new URL(window.location.href);
    var search_params = url.searchParams;

    array.forEach(element => {
        search_params.set(element.name, element.value)
    });

    url.search = search_params.toString();
    window.history.replaceState(null, null, url.toString());
}