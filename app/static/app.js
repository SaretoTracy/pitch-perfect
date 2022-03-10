let upvotebtn = document.querySelectorAll('#upvote');
let downvotebtn = document.querySelectorAll('#downVote');
let vote = document.querySelectorAll('.vote')

let input1 = document.querySelectorAll('#input1')
let input2 = document.querySelectorAll('#input2')

upvotebtn.addEventListener('click', () => {
    input1.value = parseInt(input1.value) + 1;
})
downvotebtn.addEventListener('click', () => {
    input2.value = parseInt(input2.value) + 1;
})

// for (let i = 0; i < upvotebtn.length || i < vote.length; i++) {
//     upvotebtn[i].addEventListener("click", () => {
//         input1.value = parseInt(input1.value) + 1;

//     })
// };