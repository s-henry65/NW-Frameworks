// const toggle = document.querySelector(".toggle");

// toggle.addEventListener("click", (e) => {
//     if (toggle.innerText === "Show Gold") {
//         toggle.innerText = "Hide Gold";
//     } else {
//       toggle.innerText = "Show Gold";
//     }
// });

$(document).ready(function () {
    $("#gold").hide()
    $(".toggle").click(function(){
        $("#gold").toggle();
    });
});
