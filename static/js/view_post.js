/*
This javascript is used in post/view_post.html, it lets a
professional user open up a form for writing their
answer, by clicking a button.
*/

const button = document.querySelector("#write_answer_button")

function showAnswerForm() {
    const form = document.querySelector("#answer_form")
    form.hidden = false
}

button.addEventListener("click", showAnswerForm)