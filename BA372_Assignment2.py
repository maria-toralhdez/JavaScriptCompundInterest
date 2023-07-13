#Gets user input for starting capital, low interest rate, high interest rate
#number of intervals and number of periods.
#Handles error if user enters characters and if values provided are not in range
while True:
  try:
    starting_capital = float(input("What is your starting capital ( <=1000 )?: "))
  except ValueError:
    print("Provide an integer / float value...")
    continue
	
  if starting_capital > 0 and starting_capital <= 1000:
    break
  else:
    print("Invalid starting capital(not in range), please try again...")      
	
while True:
  try:
    low_int_rate = float(input("Provide a low interest rate ( in percent! ( <=10.0 )): "))
  except ValueError:
    print("Provide a possitive integer / float value...")
    continue
	
  if  low_int_rate > 0.0 and low_int_rate <= 9.9:
    break
  else:
    print("Invalid low interest rate(not in range), please try again...")      
	
while True:
  try:
    high_int_rate = float(input("Provide a high interest rate ( in percent! ( <=10.0 )): "))
  except ValueError:
    print("Provide a possitive integer / float value...")
    continue
	
  if  high_int_rate > 0 and high_int_rate <= 10.0 and (high_int_rate > low_int_rate):
    break
  else:
    print("Invalid high interest rate(not in range or not higher than low interest rate), please try again...")      

while True:
  try:
    intervals = int(input("How many intervals ( <= 25 )?: "))
  except ValueError:
    print("Provide a possitive integer / float value...")
    continue
	
  if intervals >= 1 and intervals <= 25:
    break
  else:
    print("Invalid number of intervals(not in range), pleasy try again...")      
 

while True:
  try:
    periods = int(input("How many periods ( <= 25 )?: "))
  except ValueError:
    print("Provide a possitive integer / float value...")
    continue
	
  if periods > 0 and periods <= 25:
    break
  else:
    print("Invalid number of periods(not in range), pleasy try again...")      
  
#tries to open an HTML file, handles errors if any
def writeToHTML():
	try:
		file = open("exercise.html", "w")
	except Exception as e:
		print("Error opening file..\n", e)
		exit(1)
	#if it successfully opens the file, writes the first lines of the JavaScript code
	#into an html file called 'exercise.html'
	file.write("""<html>
<head>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript">
google.load("visualization", "1", {packages:["linechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
var data = google.visualization.arrayToDataTable([
['Period' , """)
	
	#computes the number of compund interest intervals
	interest_intervals = (high_int_rate - low_int_rate) / (intervals)
	
	#loop for the interest intervals in % form
	#calcuates values and writes them on the HTML file
	for i in range(intervals + 1):
		interest_rate = low_int_rate + i * interest_intervals
		file.write("'" + str(interest_rate) + "%'")
		if i == intervals:
			file.write("],")
		else:
			file.write(", ")
	
	#loop that goes through each period and calculates accumulated amount for each interest interval
	#calculates values an writes them on the HTML file
	for i in range(1, periods + 1):
		accum_int = [f'{i}]']
		for j in range(intervals + 1):
			interest_interval = (low_int_rate + (interest_intervals * j))/100
			accum_amount = starting_capital * (1.0 + interest_interval)**i
			accum_int.append(accum_amount)
		if i != periods:
			file.write(f'\n{accum_int},')
		else:
			file.write(f'\n{accum_int}\n]);')
	#writes last lines of the JavaScript code into the HTML file	
	file.write("""
var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
chart.draw(data, {width: 1000, height: 500, legend: 'bottom', title: 'Compound Interest Profiles'});
}
</script>
</head>
<body>
<div id="chart_div"></div>
</body>
</html>""")
	
	#closes HTML file
	file.close()
#tells user JavaScript code is in an HTML file called 'exercise.html' and tells them to
#open file on their browser
print("Writing to file 'exercise.html', open on browser")

input("press enter to quit...")
