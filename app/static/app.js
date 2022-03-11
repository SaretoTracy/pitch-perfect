let upvotebtn = document.querySelectorAll('.upvote');
let downvotebtn = document.querySelectorAll('.downVote');
let vote = document.querySelectorAll('.vote')

let input1 = document.querySelectorAll('.input1');
let input2 = document.querySelectorAll('.input2')


for (let i = 0; i < upvotebtn.length; i++) {
    upvotebtn[i].addEventListener("click", () => {
        console.log(input1[i].innerHTML++);

    })
};
for (let i = 0; i < downvotebtn.length; i++) {
    downvotebtn[i].addEventListener("click", () => {
        console.log(input2[i].innerHTML++);
    })
}