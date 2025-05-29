/*
This javascript is used in post/answer.html, it lets a professional user
click a like button and have it update the like (rating) counter on the
answer without having to leave the page.
*/

const thumbs_up_buttons = document.querySelectorAll(".thumbs-up-button")
thumbs_up_buttons.forEach(b => {
    b.addEventListener("click", likeClick)
})

function likeClick(event) {
    const button = event.currentTarget
    const answer_id = button.getAttribute("data-answer-id")

    // Send requst to the view
    fetch(`/post/like/${answer_id}/`, {
        method : "POST",
        headers : {
            "X-CSRFToken" : getCookie("csrftoken"),
            "Content-Type" : "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        // Update the number of ratings
        const span = button.querySelector("span")
        span.innerText = data.count

        // Make hand filled or not-filled depending on whether it was just liked or un-liked
        const icon = button.querySelector("i")
        if (data.already_liked) {
            const toastEl = document.querySelector(`#alreadyToast${answer_id}`)
            const toast = bootstrap.Toast.getOrCreateInstance(toastEl)
            toast.show()
        }
    })
}


// CODE RETRIEVED FROM https://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}