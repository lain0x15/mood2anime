"use strict";

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById('add_in_list').addEventListener('click', show_add_list);
});

function show_add_list() {
  document.getElementById("list_relative").classList.toggle("show");
}