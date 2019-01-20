function validate() {
    var val = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

    if (reg.test(val) == false) {
        var err = "Enter a valid email";
        document.getElementById("email_err").innerHTML = err;
        document.getElementById("email_err").style.color = "red";
    } else {
        document.getElementById("email_err").innerHTML = "Valid Email";
        document.getElementById("email_err").style.color = "green";
    }

    if (password.length <= 8) {
        document.getElementById("password_err").innerHTML =
            "Enter more than 8 characters";
        document.getElementById("password_err").style.color = "red";
    } else {
        document.getElementById("password_err").innerHTML =
            "You have entered a valid password";
        document.getElementById("password_err").style.color = "green";
    }
}
