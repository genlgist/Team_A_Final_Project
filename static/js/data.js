//accessing predict route of flask app
const url = "http://127.0.0.1:5000/predict";

// fetching the JSON data
let predict = d3.json(url)

// creating data variable
var data = [
    {
      expression: predict.Expression[0][0],
      predictscore: predict.PredictScore[0][0],
    },
    {
      expression: "surprise",
      emoscore: "23%",
    },
    {
      expression: "neutral",
      predictscore: "22%",
    }
  ];

