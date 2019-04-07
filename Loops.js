function vowelsAndConsonants(s) {
    var i;
    var vowels = ["a","e","i","o","u"];
    for (i = 0; i < s.length; i++) {
        if (vowels.indexOf(s[i]) > -1 in vowels) {
            console.log(s[i])
        }        
    }
}