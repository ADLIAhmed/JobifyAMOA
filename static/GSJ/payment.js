var inputs = document.querySelectorAll(".input-case");
function focusFunc(){
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus');
}
function blurFunc(){
    let parent = this.parentNode.parentNode;
    if(this.value == ""){
        parent.classList.remove('focus');
    }
}
inputs.forEach(input => {
    input.addEventListener("focus", focusFunc);
    input.addEventListener("blur", blurFunc);
});


function checkCreditCard(textBox,inputFilter) {
    ["input","keydown","keyup","mousedown","mouseup","select","contextmenu","drop"].forEach(function(event){
        textBox.addEventListener(event,function(){
            if(inputFilter(this.value)){
                this.oldValue = this.value;
                this.oldSelectionStart = this.selectionStart;
                this.oldSelectionEnd = this.selectionEnd;
            } else if(this.hasOwnProperty("oldValue")){
                this.value = this.oldValue;
                this.setSelectionRange(this.oldSelectionStart,this.oldSelectionEnd);
            } else {
                this.value = "";
            }
        });
    });
}
checkCreditCard(document.getElementsByClassName("creditCard"),function(value){
    return /^\dddd dddd dddd dddd$/.test(value);
})