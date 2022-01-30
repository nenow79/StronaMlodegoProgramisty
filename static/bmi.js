function myFunction() {
    var waga = document.getElementById('waga').value;
    var wzrost = document.getElementById('wzrost').value/100;
    var bmi = (waga/(wzrost*wzrost)).toFixed(1);
    document.getElementById("myOutput").innerHTML = bmi;
    var judge = '';
    if ((bmi >= 18.5) && (bmi <= 24.9)) {
        judge = "Waga prawidowa!";
    } else if (bmi <= 18.4){
        judge = "Niedowaga";
    }else if ((bmi >= 25) && (bmi <= 29.9)){
        judge = "Nadwaga!";
    } else if ((bmi >= 30) && (bmi <= 34.9)){
        judge = "Otylosc I stopnia";
    } else if (bmi >= 35){
        judge = "Otylosc II lub III stopnia";
    }else {
        var judge = ''
    }
    
    document.getElementById("myOutput2").innerHTML = judge;
}