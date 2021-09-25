function predict(){
    const url = "/predict";

    console.log("calling d3");
    d3.json(url).then(function(response){
        console.log(response);
        const data = response;
        
        tabulate(data, ['Expression', 'EmoScore']);
        
    });
}

//function to tabulate data
function tabulate(data, columns) {
    console.log(data);
    var table = d3.select('table')
    var thead = table.append('thead')
    var tbody = table.append('tbody');

    // append the header row
    thead.append('tr')
        .selectAll('th')
        .data(columns).enter()
        .append('th')
        .text(function(column) { return column; });

    // create a row for each object in the data
    var rows = tbody.selectAll('tr')
        .data(data)
        .enter()
        .append('tr');

    // create a cell in each row for each column
    var cells = rows.selectAll('td')
        .data(function(row) {
            return columns.map(function(column) {

                return { column: column, value: row[column] };
            });
        })
        .enter()
        .append('td')
        .text(function(d) { return d.value; });

    return table;
}

