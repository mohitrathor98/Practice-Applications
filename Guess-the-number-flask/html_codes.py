header = """
<!DOCTYPE html>
<html style="background-color: #86A3B8;">
  <head>
    <title>Guess the Number!</title>
  </head>
"""

footer= """
</body>
</html>
"""


input_form = """
<form name="inputForm" action="/submit-form" method="post">
    <label for="text-box">Enter you input here: </label>
    <input type="text" id="user_choice" name="choice-field">
    <input type="submit" value="Submit">
</form>
"""

landing_body = header + """
<body>
<h1 >Guess the number between 0 and 9!!</h1>
<iframe src="https://giphy.com/embed/fDUOY00YvlhvtvJIVm" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br>
""" + input_form + footer

low_value_body = header + """
<h1 style="color: red">Value too low, try again!!!</h1>
<iframe src="https://giphy.com/embed/iIppd7C1OmVNKwuHZB" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br>
""" + input_form + footer

high_value_body = header + """
<h1 style="color: violet">Too High, Go lower!!!</h1>
<iframe src="https://giphy.com/embed/l4FB8UWQN6SqpPa2A" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br>
""" + input_form + footer

success_body = header + """
<h1 style="color: violet">Congrats!! You Found It.</h1>
<iframe src="https://giphy.com/embed/2m1lj8p8v6JcWpREtL" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br><br>
<form name="restart-game" action="/game-restart" method="post">
  <input type="submit" value="Restart!!!">
</form>
""" + footer

error_body = header + """
<h1>Please enter values between 0 to 9</h1>
<iframe src="https://giphy.com/embed/nR4L10XlJcSeQ" width="480" height="412" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br>
""" + input_form + footer

