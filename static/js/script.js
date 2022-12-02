
    // function js_test(){
    //   console.log("function called");
    //   let giorno1 = document.getElementsByClassName("day1");
    //   console.log(giorno1);
    //   console.log(giorno1[0].innerText);
    //   for (var i = 0; i < giorno1.length; i++) {
    //     let testo = giorno1[i]["innerText"];
    //     console.log(testo)
    //   }
    // };
    // js_test();
    // let cacca = document.getElementsByClassName("day2").innerHtml
    // for (i in cacca){
    //     console.log(i)
    // }
    // console.log(cacca)
    let collection = document.getElementsByClassName("day3");
    console.log(collection)
    let text = collection.innerHtml;
    console.log(text)

    var x = document.getElementsByClassName("day1");
    
    console.log(x)
for (var i = 0; i < x.length; i++) {
    console.log(x.item(i))
    x[i].style.color = "blue";
    console.log(x[i])
}