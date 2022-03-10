let upvotebtn = document.querySelectorAll('#upvote');
let downvotebtn = document.querySelectorAll('#downVote');
let vote = document.querySelectorAll('.vote')

let input1 = document.querySelectorAll('#input1')
let input2 = document.querySelectorAll('#input2')


for (let i = 0; i > upvotebtn.length || i > vote.length; i++) {
    upvotebtn[i].addEventListener("click", () => {
        input1.value = parseInt(input1.value) + 1;

    })
};