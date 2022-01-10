window.addEventListener("load" , function (){
    draw_pie("income");
    draw_pie("spending");
});

function draw_pie(target){

    let elem_categories = $("." + target + "_category");
    let elem_totals     = $("." + target + "_total");

    let categories      = [];
    let totals          = [];

    //jQueryで手に入れた要素をループする。(※この時取り出した要素はjQueryのオブジェクトではない点に注意)
    //カテゴリ名と金額をそれぞれリストに格納(金額は円とカンマを消して、数値型に仕立てる)
    for (let c of elem_categories){
        categories.push(c.innerText);
    }
    for (let t of elem_totals){
        totals.push(Number(t.innerText.replace(",","").replace("円","")));
    }

    console.log(categories);
    console.log(totals    );
    
    //色作成(収入の場合は緑系、支出の場合は赤系)
    let colors  = []
    var rgb     = 255;
    var minus   = 255/categories.length;
    
    if (target == "income"){
        for (let c of categories){
            colors.push("rgb(100, " + String(rgb)+ ", 100)");
            rgb -= minus;
        }
    }
    else{
        for (let c of categories){
            colors.push("rgb(" + String(rgb)+ ",0,0)");
            rgb -= minus;
        }
    }

    //描画
    const ctx = document.getElementById("category_graph_" + target ).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: categories,
            datasets: [{
                data: totals,
                backgroundColor: colors,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    type:"linear",
                },
                x: {
                    beginAtZero: true,
                    type:"linear",
                }
            }
        }
    });
}
