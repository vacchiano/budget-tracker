// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

const categoryData = JSON.parse(document.getElementById('categories-data').textContent);
// console.log(categoryData);

const categories = categoryData.map(data => data.category)
const amounts = categoryData.map(data => data.amount == null ? 0.00 : parseFloat(data.amount))
console.log(categories, amounts);

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: categories,
    datasets: [{
      data: amounts,
      backgroundColor: ['blue', 'orange', 'green', 'red', 'yellow', 'teal', 'violet', 'grey', 'purple', 'indigo', 'skyblue'],
    }],
  },
  options: {
    legend: {
      display: false
    }
  }
});
