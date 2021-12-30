function check_frm(){
    var name = document.frm.name.value;
    var phone = document.frm.phone.value;
    var amount = document.frm.amount.value;
    var weight = document.frm.weight.value;
    var rate = document.frm.rate.value;
    
    var reg = "^[a-zA-Z ]*$";
    

    if (name=="" && phone=="" && amount=="" && weight=="" && rate==""){
        alert("Field Cannot be Empty")
    }
    if(name.match(reg)){
        document.getElementById("error").innerHTML =" ";
    }
    else{
        document.getElementById("error").innerHTML ="Please enter Alphabets";
    }
}

function on_delete(){
    alert("Are you sure you Want to delete this entry")
}



