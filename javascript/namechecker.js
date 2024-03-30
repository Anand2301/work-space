let name=prompt("enter your name:");
function check(){
    return /^[a-zA-Z]+$/.test(name)
}
function greet(){
    if (check()){
        console.log("hi"+name);
    }else{
        console.log("please enter a valid name");
    }
}
greet();
