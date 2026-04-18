let string = "";
let buttons=document.querySelectorAll(".button");
Array.from(buttons).forEach((button)=>{
    button.addEventListener('click',(event)=>{
        string = string + event.target.innerHTML;
        kgDisplay.value = string;
    });
});

let kgDisplay = document.querySelector(".kg-display");
let monDisplay = document.querySelector(".mon-display");

let clearBtn = document.querySelector("#clearBtn").addEventListener('click',()=>{
    string ="";
    kgDisplay.value = string;
    monDisplay.value = string;
});

let equalBtn = document.querySelector("#equalBtn");
equalBtn.addEventListener("click",()=>{
    let Value = kgDisplay.value;
    let x= Value/40;
    let y= parseInt(x);
    let z= x-y;
    if (z==0) {
        let  finalValue = `${x}   mon`
        monDisplay.value = finalValue;
    } else {
        let n= z*40;
        let  finalValue = `${y}   mon    ${n}  kg `
        monDisplay.value = finalValue;
    } 
});