var ctx = document.getElementById("r3").getContext("2d");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['A10', 'TECNO POP', 'SAMSUNG S7', 'ITEL', 'KA TORCH', 'IPHONE 7'],
        datasets: [{
            label: 'Like',
            data: [50, 10, 210, 28, 10, 200],
            backgroundColor: [
                'rgba(0,255,0)'

            ],
            borderColor: 'rgb(41, 155, 99)',
            borderWidth: 1
        },
        {
            label: 'Dislike',
            data: [50, 190, 20, 800, 18, 20],
            backgroundColor: [
                'rgba(255,0,0)'

            ],
            borderColor: 'rgb(41, 155, 99)',
            borderWidth: 1
        }
    ]
    },
    options: {
        responsive: true
    }
});
