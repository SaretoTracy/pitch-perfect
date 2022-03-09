let upvotebtn = document.querySelector('#upvote');
let downvotebtn = document.querySelector('#downvote');

let input1 = document.querySelector('#input1')
let input2 = document.querySelector('#input2')

upvotebtn.addEventListener('click', () => {
    input1.value = parseInt(input1.value) + 1;
})