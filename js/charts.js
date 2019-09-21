var ctx1 = document.getElementById("allot-graph").getContext('2d');
var ctx2 = document.getElementById("demand-graph").getContext('2d');


var datalabels = Chart.plugins.getAll().filter(function(p) {
  return p.id === 'datalabels';
})[0];


Chart.defaults.global.defaultFontColor = 'black';
Chart.defaults.global.defaultFontSize = 14;
//disable all datalabels globally
Chart.plugins.unregister(datalabels);


var line_data = {
                labels:['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December'],
                datasets:[
                    {
                   label:'C1',
                    fill:false,
                    backgroundColor: "green",
                    borderColor: "green",
                    data: [65, 59, 80, 81, 56, 55]
                    }, {
                    label:'C2',
                    fill:false,
                    backgroundColor: "red",
                    borderColor: "red",
                    data: [60, 55, 70, 91, 65, 60]                    
                        
                    },{
                    label:'C3',
                    fill:false,
                    backgroundColor: "black",
                    borderColor: "black",
                    data: [62, 57, 72, 89, 63, 58]                    
                        
                    },{
                    label:'C4',
                    fill:false,
                    backgroundColor: "violet",
                    borderColor: "violet",
                    data: [55, 65, 91, 70, 60, 65]                    
                        
                    },{
                    label:'C5',
                    fill:false,
                    backgroundColor: "teal",
                    borderColor: "teal",
                    data: [70, 45, 80, 81, 75, 50]                    
                        
                    } 
                ]   
                
                }
    
                
            
    
var line_options = {
                scales:{
                    yAxes:[{
                        
                        ticks:{
                            beginAtZero:true
                        },
                        scaleLabel:{
                            display:true,
                            labelString:"units",
                            fontSize:20
                        }
                        
                    }]
                },
            
            title:{
                display:true,
                text:"Allotment FY19-20"
            },
    
            plugins:{lables:false}
    
            }

        
    
var monthlyAllotmentchart = new Chart(ctx1, {
            
            type:'line',
            data:line_data,
            options:line_options,
        });


var demand_data = {
    labels:['Company1', 'Company2', 'Company3', 'Company4', 'Company5'],
    datasets:[{
        fill:true,
        backgroundColor:['red','pink', 'yellow', 'green', 'blue'],
        data:[10,20,40,20,10],
        
    }]
    
}
var demand_option ={
//    tooltips: {
//         enabled: false
//    },
    
    title:{
        display:true,
        text:"Customer demand"
    },
    plugins:{
        lables:true
        
        
    }
   
}
var demandPieChart = new Chart(ctx2, {
    type: 'pie',
    data: demand_data,
    options: demand_option
});