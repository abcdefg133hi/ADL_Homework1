window.alert("猜猜這是什麼呢")
const b1 = document.getElementById("btn")
const i1 = document.getElementById("inp")
let name = "hello"
let best_friend = "aha"
const true_best_friend = "黃偉翔"
function getName()
{
    name = document.getElementById("inp").value;
    //document.getElementById("box").innerHTML = name;
}
function getBest_Friend()
{
    best_friend = document.getElementById("inp2").value
}
function click_btn1()
{
    getName()
    const Step2 = document.getElementById("step2")
    Step2.innerHTML = "<p>請輸入您最好的朋友（請以中文書寫）：</p> <input type=\"text\" id=\"inp2\"/> <button type=\"button\" onclick=\"click_btn2()\">確認</button>"
}

function click_btn2()
{
    getBest_Friend()
    //document.getElementById("box").innerHTML = best_friend;
    if(true_best_friend===best_friend)
    {
        const Step3 = document.getElementById("step3")
        const Best = document.getElementById("best")
        Best.innerHTML = "Great!"
        Step3.innerHTML = "<button type=\"button\" onclick=\"window.location.href='whtiee.html'\" class='button'>點我</button>"
    }
    else
    {
        const Best = document.getElementById("best")
        Best.innerHTML = "Oh no! 請你不要說謊喔！重新輸入一次吧！"
    }
}

function click_btns()
{
    getName()
    const Temp = document.getElementById("temp")
    Temp.innerHTML = "<button id=\"btn4\" onclick=\"click_btn4()\">按下去會有驚喜</button>"
}

function click_btn4()
{
    const Step41 = document.getElementById("step41")
    const Step42 = document.getElementById("step42")
    const Step43 = document.getElementById("step43")
    const Step44 = document.getElementById("step44")
    const Step45 = document.getElementById("step45")
    const Step46 = document.getElementById("step46")
    const Step47 = document.getElementById("step47")
    const Step48 = document.getElementById("step48")
    Step41.innerHTML = name[0]
    Step42.innerHTML = name[1]
    Step43.innerHTML = name[2]
    Step44.innerHTML = "生"
    Step45.innerHTML = "日"
    Step46.innerHTML = "快"
    Step47.innerHTML = "樂"
    Step48.innerHTML = "！"
}




